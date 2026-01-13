import os

from data import Info, ACCTEXT, COMMANDSLIST, set_ObjName, set_ObjDescription, set_ObjStock, set_ObjID, set_ObjVersion, Component, component_to_dict , set_filename, LABELS
from CLIUI import LogoDraw, LineUI, bcolors
from jsonprocess import write_json, remove_json, create_json_parameters, view_json, validate_name_id_json
from notifications import NotificationCall, GetCorrectValue, GetDirectory


# Defaults
MaxPage = (len(COMMANDSLIST.Commands) + 9) // 10 


# ==================
# Help Commands
# ==================


# Release Notes Command
def ReleaseNotes():
    LineUI()
    for item in Info.DevNotes:
        print(item)
    LineUI()


# About Command
def AboutCommand():
    LineUI()
    LogoDraw()
    for item in Info.AboutStrings:
        print(item)
    LineUI()


# Help List
def HelpCommand():   
    LineUI()
    for item in Info.HelpStrings:
        print(item)
    LineUI()


# Open Command Help
def OpenCommandHelp():
    LineUI()
    for item in Info.OpenCommandHelpStrings:
        print(item)
    LineUI()


# Create Command Help
def CreateCommandHelp():
    LineUI()
    for item in Info.CreateCommandHelpStrings:
        print(item)
    LineUI()


# Purge Command Help
def PurgeCommandHelp():
    LineUI()
    for item in Info.PurgeCommandHelpStrings:
        print(item)
    LineUI()


# Command Display Mode Commmand
def ComDisplay(CurrentPage=1):
    LineUI()
    print(f'The Complete List Of Commands {bcolors.BOLD}(Currently Displaying 10 Elements){bcolors.ENDC}: ')
        
    start_index = (CurrentPage - 1) * 10
    end_index = min(start_index + 10, len(COMMANDSLIST.Commands)) 
        
    for i in range(start_index, end_index):
        print(f"{i + 1}. {COMMANDSLIST.Commands[i]}")

    print(f'Page ({bcolors.BOLD}{CurrentPage}/{MaxPage}{bcolors.ENDC})                                       {bcolors.OKCYAN}/next{bcolors.ENDC} - {bcolors.OKCYAN}/prev{bcolors.ENDC} - {bcolors.OKCYAN}/exit{bcolors.ENDC}')
    LineUI()


# Command Mode Command
def ComCom(CurrentPage=1):
    while True:

        ComDisplay(CurrentPage)

        while True :
            command = GetCommand()

            if command == "/exit":
                return

            elif command == "/next" and CurrentPage < MaxPage:
                CurrentPage += 1
                ComDisplay(CurrentPage)

            elif command == "/next" and CurrentPage == MaxPage:
                MsgMode = "error-max-page"
                NotificationCall(MsgMode, Info.FileName)

            elif command == "/prev" and CurrentPage > 1:
                CurrentPage -= 1
                ComDisplay(CurrentPage)

            elif command == "/prev" and CurrentPage == 1:
                MsgMode = "error-min-page"
                NotificationCall(MsgMode, Info.FileName)

            elif command == "/open":
                OpenCommandHelp()

            elif command == "/create":
                CreateCommandHelp()

            elif command == "/purge":
                PurgeCommandHelp()

            else:
                MsgMode = "error-unknown-command"
                NotificationCall(MsgMode, Info.FileName)


# =======================
# Command Modes
# =======================


# Options When A File Is Loaded
def FileMode(CurrentPage, file_path):
    command = GetCommand()
    while True:

        if command == "/exit":
            break


        elif command == "/commands":
            Info.ACCESS = ACCTEXT.get_access_text("mode-com", Info.FileName)
            ComCom(CurrentPage)
            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)


        elif command == "/add":
            comp = Component('', '', 0, 0, '')

            # Set Object Name
            search_mode = "name"
            Info.ACCESS = ACCTEXT.get_access_text("add-name", Info.FileName)

            while True:
                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the name of the object you want to create : ')
                ObjName = input(f'{Info.ACCESS}')

                if ObjName == "/exit":
                    Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                    break

                exists = validate_name_id_json(file_path, ObjName, search_mode)

                if exists:
                    NotificationCall("error-item-name-already-exists", ObjName)
                    continue


                set_ObjName(comp, ObjName)
                break

            

            # Set Object Description
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the description of the object {bcolors.OKGREEN}{ObjName}{bcolors.ENDC} you want to create : ')
            Info.ACCESS = ACCTEXT.get_access_text("add-desc", Info.FileName)
            ObjDescription = input(f'{Info.ACCESS}')
            set_ObjDescription(comp, ObjDescription)
            if ObjDescription == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                break

            # Set Object Stock
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the stock of the object {bcolors.OKGREEN}{ObjName}{bcolors.ENDC} you want to create : ')
            Info.ACCESS = ACCTEXT.get_access_text("add-stock", Info.FileName)
            
            while True:
                stock_input = input(f'{Info.ACCESS}')

                if stock_input == "/exit":
                    ObjStock = None
                    break

                try:
                    ObjStock = int(stock_input)

                    if ObjStock < 0:
                        GetCorrectValue("be greater or equal to 0")
                        NotificationCall("error-invalid-value", Info.FileName)
                        continue

                    break

                except ValueError:
                    GetCorrectValue("be an integer")
                    NotificationCall("error-invalid-value", Info.FileName)
                    continue



            set_ObjStock(comp, ObjStock)


            # Set Object ID
            Info.ACCESS = ACCTEXT.get_access_text("add-id", Info.FileName)

            while True:
                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the ID of the object {bcolors.OKGREEN}{ObjName}{bcolors.ENDC} you want to create : ')
                ObjID = input(f'{Info.ACCESS}')

                if ObjID == "/exit":
                    Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                    break  # exit /add cleanly

                # Check if ID already exists
                search_mode = "id"
                exists = validate_name_id_json(file_path, ObjID, search_mode)

                if exists:
                    NotificationCall("error-item-id-already-exists", ObjID)
                    continue  # ask again

                # ID is valid and unique
                set_ObjID(comp, ObjID)
                break


            # Set Object Version (Automatic)
            ObjVersion = Info.VERSION

            set_ObjVersion(comp, ObjVersion)


            # Final Push
            push = component_to_dict(comp)

            write_json(push, file_path)
            
            GetDirectory(Info.FileName)
            NotificationCall("success-obj-add", ObjID)

            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)


        elif command == "/remove":
            
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the way you want to identify the object you wish to {bcolors.FAIL}remove/delete{bcolors.ENDC} (either by {bcolors.PURPLE}/id{bcolors.ENDC} or {bcolors.PURPLE}/name{bcolors.ENDC}) : ')
            Info.ACCESS = ACCTEXT.get_access_text("remove", Info.FileName)
            command = GetCommand()

            # Answer Checking
            while command != "/exit" and command != "/id" and command != "/name":
                GetCorrectValue("/exit || /id || /name")
                NotificationCall("error-invalid-value",Info.FileName)

                command = GetCommand()
  
            if command == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                break
            
            # ID Case
            elif command == "/id":
                search_mode = "id"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}ID{bcolors.ENDC} of the object you want to {bcolors.FAIL}remove/delete{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text(f"remove-{search_mode}", Info.FileName)

                while True:
                    search_key = GetCommand()
                    if search_key == "/exit":
                        Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                        break

                    exists = validate_name_id_json(file_path, search_key, search_mode)
                    if not exists:
                        NotificationCall("error-invalid-obj", search_key)
                        continue

                    remove_json(file_path, search_key, search_mode)
                    GetDirectory(Info.FileName)
                    NotificationCall("success-obj-remove", search_key)
                    break



            # Name Case
            elif command == "/name":
                search_mode = "name"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}ID{bcolors.ENDC} of the object you want to {bcolors.FAIL}remove/delete{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text(f"remove-{search_mode}", Info.FileName)

                while True:
                    search_key = GetCommand()
                    if search_key == "/exit":
                        Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                        break

                    exists = validate_name_id_json(file_path, search_key, search_mode)
                    if not exists:
                        NotificationCall("error-invalid-obj", search_key)
                        continue

                    remove_json(file_path, search_key, search_mode)
                    GetDirectory(Info.FileName)
                    NotificationCall("success-obj-remove", search_key)
                    break

            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
        

        elif command == "/view":
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the way you want to identify the object you wish to {bcolors.PURPLE}view{bcolors.ENDC} (either by {bcolors.PURPLE}/id{bcolors.ENDC} or {bcolors.PURPLE}/name{bcolors.ENDC}) : ')
            Info.ACCESS = ACCTEXT.get_access_text("view-obj", Info.FileName)
            command = GetCommand()

            # Answer Checking
            while command != "/exit" and command != "/id" and command != "/name":
                correctvalue = "/exit || /id || /name"
                MsgMode = "error-invalid-value"
                GetCorrectValue(correctvalue)
                NotificationCall(MsgMode,Info.FileName)

                command = GetCommand()
  
            # Exit Case
            if command == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                break


            # ID Case
            elif command == "/id":
                search_mode = "id"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}ID{bcolors.ENDC} of the object you want to {bcolors.PURPLE}view{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text("view-obj-id", Info.FileName)
                while True:
                    command = GetCommand()

                    search_key = command

                    result = view_json(file_path, search_key, search_mode)

                    if result == -1:
                        MsgMode = "error-invalid-obj"
                        NotificationCall(MsgMode, search_key)
                        GetCommand()
                        search_key = command
                        break

                    else:
                        LineUI()
                        for key, label in LABELS.items():
                            if key in result:
                                print(f"{label}: {result[key]}")
                        LineUI()
                        break

            # Name Case
            elif command == "/name":
                search_mode = "name"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}Name{bcolors.ENDC} of the object you want to {bcolors.PURPLE}view{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text("view-obj-name", Info.FileName)
                while True:
                    command = GetCommand()

                    search_key = command

                    result = view_json(file_path, search_key, search_mode)

                    if result == -1:
                        MsgMode = "error-invalid-obj"
                        NotificationCall(MsgMode, search_key)
                        GetCommand()
                        search_key = command
                        break

                    else:
                        LineUI()
                        for key, label in LABELS.items():
                            if key in result:
                                print(f"{label}: {result[key]}")
                                if key == "obj_version" and result[key] != Info.VERSION:
                                    MsgMode = "notice-obj-version"
                                    NotificationCall(MsgMode, search_key)
                        LineUI()
                        break

            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)


        else:
            MsgMode = "error-unknown-command"
            NotificationCall(MsgMode, Info.FileName)

        command = GetCommand()

    Info.ACCESS = ACCTEXT.get_access_text("file")


# =======================
# Commands
# =======================


# Open Command
def OpenCommand(CurrentPage):
    Info.ACCESS = ACCTEXT.get_access_text("open")

    command = GetCommand()

    file_path = os.path.join(Info.folder_path, command)

    if os.path.exists(file_path):
        Info.FileName, FileExtension = os.path.splitext(command)

        set_filename(Info.FileName)

        if FileExtension == ".json":
            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
            
            MsgMode = "success-file-open"
            NotificationCall(MsgMode, Info.FileName)
        else:
            MsgMode = "error-wrong-file"
            NotificationCall(MsgMode, Info.FileName)

            return
        
    else:
        if command == "/exit":
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return
        
        else:
            MsgMode = "error-directory-not-found"
            NotificationCall(MsgMode, Info.FileName)
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return

    FileMode(CurrentPage, file_path)

    Info.ACCESS = ACCTEXT.get_access_text("default")
    return


# Create Command
def CreateCommand(CurrentPage):
    Info.ACCESS = ACCTEXT.get_access_text("create")

    command = GetCommand()

    if command == "/exit":
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    set_filename(command)

    if Info.FileName.endswith(".json"):
        Info.FileName = Info.FileName[:-5]

    file_path = os.path.join(Info.folder_path, f"{Info.FileName}.json")

    if not os.path.exists(Info.folder_path):
        try:
            os.makedirs(Info.folder_path, exist_ok=True)
            MsgMode = "notice-directory-added"
            NotificationCall(MsgMode, Info.FileName)

        except PermissionError:
            MsgMode = "error-no-permission"
            NotificationCall(MsgMode, Info.FileName)

            Info.ACCESS = ACCTEXT.get_access_text("default")
            return

    elif os.path.exists(file_path):
        MsgMode = "error-file-already-exists"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    try:
        create_json_parameters(file_path)
        
        MsgMode = "success-file-add"
        NotificationCall(MsgMode, Info.FileName)

    except PermissionError:
        MsgMode = "error-no-permission"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    FileMode(Info.CurrentPage, file_path)

    Info.ACCESS = ACCTEXT.get_access_text("default")


# Purge Command
def PurgeCommand():
    Info.ACCESS = ACCTEXT.get_access_text("purge")

    command = GetCommand()

    if command == "/exit":
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    set_filename(command)

    file_path = os.path.join(Info.folder_path, command)

    if not os.path.exists(Info.folder_path):
        LineUI()
        print(f'{bcolors.WARNING}Error: Database folder {bcolors.PURPLE}{Info.folder_path}{bcolors.WARNING} does not exist.{bcolors.ENDC}')
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    if not os.path.exists(file_path):
        MsgMode = "error-directory-not-found"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.FileName, FileExtension = os.path.splitext(command)
    set_filename(Info.FileName)

    if FileExtension != ".json":
        MsgMode = "error-no-permission"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.ACCESS = ACCTEXT.get_access_text("filedelete", Info.FileName)
    MsgMode = "verify-command"
    NotificationCall(MsgMode, Info.FileName)

    command = GetCommand()
    if command == "YES":
        try:
            os.remove(file_path)
            
            MsgMode = "success-file-purge"
            NotificationCall(MsgMode, Info.FileName)

            Info.ACCESS = ACCTEXT.get_access_text("default")

            return
        
        except PermissionError:
            MsgMode = "error-no-permission"
            NotificationCall(MsgMode, Info.FileName)
    else:
        MsgMode = "notice-purge-canceled"
        NotificationCall(MsgMode, Info.FileName)

    while True:
        command = GetCommand()
        if command == "/exit":
            break
        else:
            MsgMode = "verify-command"
            NotificationCall(MsgMode, Info.FileName)

    Info.ACCESS = ACCTEXT.get_access_text("default")


# Vies Command
def ViewCommand():
    Info.ACCESS = ACCTEXT.get_access_text("view")

    command = GetCommand()

    if command == "/exit":
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    set_filename(command)

    file_path = os.path.join(Info.folder_path, command)

    if not os.path.exists(Info.folder_path):
        MsgMode = "error-database-not-found"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    if not os.path.exists(file_path):
        MsgMode = "error-directory-not-found"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.FileName, FileExtension = os.path.splitext(command)
    set_filename(Info.FileName)

    if FileExtension != ".json":
        MsgMode = "error-no-permission"
        NotificationCall(MsgMode, Info.FileName)

        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.ACCESS = ACCTEXT.get_access_text("view", Info.FileName)
    MsgMode = "verify-command"
    NotificationCall(MsgMode, Info.FileName)

    command = GetCommand()
    if command == "YES":
        try:
            os.remove(file_path)
            
            MsgMode = "success-file-purge"
            NotificationCall(MsgMode, Info.FileName)

            Info.ACCESS = ACCTEXT.get_access_text("default")

            return
        
        except PermissionError:
            MsgMode = "error-no-permission"
            NotificationCall(MsgMode, Info.FileName)
    else:
        MsgMode = "notice-purge-canceled"
        NotificationCall(MsgMode, Info.FileName)

    while True:
        command = GetCommand()
        if command == "/exit":
            break
        else:
            MsgMode = "verify-command"
            NotificationCall(MsgMode, Info.FileName)

    Info.ACCESS = ACCTEXT.get_access_text("default")


# Frequently Accessible Functions
def GetCommand():
    command = input(f'{Info.ACCESS}')

    return command