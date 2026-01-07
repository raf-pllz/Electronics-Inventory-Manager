import os

from data import Info, bcolors, ACCTEXT, COMMANDSLIST, set_ObjName, set_ObjDescription, set_ObjStock, set_ObjID, Component, component_to_dict , set_filename
from CLIUI import LogoDraw, LineUI
from jsonprocess import write_json, remove_json, create_json_parameters
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
            # Default comp
            comp = Component('','',0,0)

            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the name of the object you want to create : ')
            Info.ACCESS = ACCTEXT.get_access_text("add-name", Info.FileName)
            ObjName = input(f'{Info.ACCESS}')
            set_ObjName(comp, ObjName)
            if ObjName == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
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
                        correctvalue = "be greater or equal to 0"
                        MsgMode = "error-invalid-value"
                        GetCorrectValue(correctvalue)
                        NotificationCall(MsgMode, Info.FileName)
                        continue

                    break

                except ValueError:
                    correctvalue = "be an integer"
                    MsgMode = "error-invalid-value"
                    GetCorrectValue(correctvalue)
                    NotificationCall(MsgMode, Info.FileName)
                    continue



            set_ObjStock(comp, ObjStock)


            # Set Object ID
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the ID of the object {bcolors.OKGREEN}{ObjName}{bcolors.ENDC} you want to create : ')
            Info.ACCESS = ACCTEXT.get_access_text("add-id", Info.FileName)
            ObjID = input(f'{Info.ACCESS}')
            if ObjID == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                break

            set_ObjID(comp, ObjID)

            push = component_to_dict(comp)

            write_json(push, file_path)
            
            MsgMode = "success-obj-add"
            GetDirectory(Info.FileName)
            NotificationCall(MsgMode, ObjID)

            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)

        # Command /remove
        elif command == "/remove":
            
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the way you want to identify the object you wish to {bcolors.FAIL}remove/delete{bcolors.ENDC} (either by {bcolors.PURPLE}/id{bcolors.ENDC} or {bcolors.PURPLE}/name{bcolors.ENDC}) : ')
            Info.ACCESS = ACCTEXT.get_access_text("remove", Info.FileName)
            GetCommand()

            # Answer Checking
            while command != "/exit" and command != "/id" and command != "/name":
                correctvalue = "/exit || /id || /name"
                MsgMode = "error-invalid-value"
                NotificationCall(MsgMode, Info.FileName)

                command = GetCommand()
  
            if command == "/exit":
                Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
                break
            
            # ID Case
            elif command == "/id":
                search_mode = "id"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}ID{bcolors.ENDC} of the object you want to {bcolors.FAIL}remove/delete{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text("remove-id", Info.FileName)
                while True:
                    command = GetCommand()

                    search_key = command

                    result = remove_json(file_path, search_key, search_mode)

                    if result == -1:
                        MsgMode = "error-invalid-obj"
                        NotificationCall(MsgMode, search_key)
                        GetCommand()
                        search_key = command

                    elif result == 0:
                        MsgMode = "success-obj-remove"
                        GetDirectory(Info.FileName)
                        NotificationCall(MsgMode, ObjID)
                        break


            # Name Case
            elif command == "/name":
                search_mode = "name"

                print(f'{bcolors.OKGREEN}{bcolors.BOLD}Enter{bcolors.ENDC} the {bcolors.BOLD}NAME{bcolors.ENDC} of the object you want to {bcolors.FAIL}remove/delete{bcolors.ENDC} : ')
                Info.ACCESS = ACCTEXT.get_access_text("remove-name", Info.FileName)
                while True:
                    command = GetCommand()

                    search_key = command

                    result = remove_json(file_path, search_key, search_mode)

                    if result == -1:
                        MsgMode = "error-invalid-obj"
                        NotificationCall(MsgMode, search_key)
                        GetCommand()
                        search_key = command

                    elif result == 0:
                        MsgMode = "success-obj-remove"
                        GetDirectory(Info.FileName)
                        NotificationCall(MsgMode, ObjID)
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


# Frequently Accessible Functions
def GetCommand():
    command = input(f'{Info.ACCESS}')

    return command