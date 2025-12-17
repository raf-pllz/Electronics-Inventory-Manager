import os
import json
from data import Info, bcolors, Logo, ACCTEXT, set_filename


# List of Commands
Commands = [
    f"{bcolors.OKCYAN}/about{bcolors.ENDC}          | Displays a list of information about this software",
    f"{bcolors.OKCYAN}/commands{bcolors.ENDC}       | Displays a list of the commands available",
    f"{bcolors.OKCYAN}|- /ANYCOMMAND{bcolors.ENDC}  | Write any command to get help on how to use it",
    f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}        | Exits The Commands Display Mode\n",

    f"{bcolors.OKCYAN}/help{bcolors.ENDC}           | Gives a list of the most important/useful commands",
    f"{bcolors.OKCYAN}/quit{bcolors.ENDC}           | Quits and closes the terminal window",
    f"{bcolors.OKCYAN}/open{bcolors.ENDC}           | Opens a (.json) file in the Vault Directory",
    f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}        | Exits The Open Mode\n",

    f"{bcolors.OKCYAN}/create{bcolors.ENDC}         | Creates a (.json) file in the Vault Directory",
    f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}       | Exits The Create Mode\n",

    f"{bcolors.OKCYAN}/purge{bcolors.ENDC}         | Remove a (.json) file from the Vault Directory",
    f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}       | Exits The Purge Mode\n",
]

MaxPage = (len(Commands) + 9) // 10 


# UI Decorations
def LineUI():
    print("=" * 70)


# Databases Folder Initiate
if not os.path.exists(Info.folder_path):
    os.makedirs(Info.folder_path)
    LineUI()
    print(f'{bcolors.OKGREEN}{bcolors.BOLD}Notice!{bcolors.ENDC} Performed a {bcolors.PURPLE}Database{bcolors.ENDC} vault/folder creation (as there wasn\'t any other present)')


# Launch Process
def StartManager():
    LineUI()
    print("Welcome To Creative Tools - Electronics Inventory Manager")
    print(f'Developed By Rafail Palalakis, Version : {bcolors.PURPLE}{Info.VERSION}{bcolors.ENDC}')
    print("To Get Started Try One Of These Commands Below:")


# Help List
def HelpCom():   
    LineUI()
    print(f'{bcolors.OKCYAN}/help{bcolors.ENDC}             | Gives a list of the most important/useful commands')
    print(f'{bcolors.OKCYAN}/quit{bcolors.ENDC}             | Quits and closes the terminal window')
    print(f'{bcolors.OKCYAN}/about{bcolors.ENDC}            | Displays a list of information about this software')
    print(f'{bcolors.OKCYAN}/commands{bcolors.ENDC}         | Displays a list of the commands available')
    LineUI()


# About Command
def AboutCom():
    LineUI()
    for i in Logo.HorVersion:
        print(i)

    print(f'Software Version : {bcolors.PURPLE}{Info.VERSION}{bcolors.ENDC}')
    print(f'Release Date : {bcolors.PURPLE}{Info.DATE}{bcolors.ENDC}')
    print("© 2025, Made By Rafail Palalakis, All Rights Reserved")
    print("Built with ❤️  using Python 3")
    print("My LinkedIn Page : https://www.linkedin.com/in/raf-pllz/")
    LineUI()


# Command Display (Paged)
def ComCom(CurrentPage=1):
    LineUI()
    print(f'The Complete List Of Commands {bcolors.BOLD}(Currently Displaying 10 Elements){bcolors.ENDC}: ')
    
    start_index = (CurrentPage - 1) * 10
    end_index = min(start_index + 10, len(Commands)) 
    
    for i in range(start_index, end_index):
        print(f"{i + 1}. {Commands[i]}")

    print(f'Page ({bcolors.BOLD}{CurrentPage}/{MaxPage}{bcolors.ENDC})                                       {bcolors.OKCYAN}/next{bcolors.ENDC} - {bcolors.OKCYAN}/prev{bcolors.ENDC} - {bcolors.OKCYAN}/exit{bcolors.ENDC}')
    LineUI()

# Open Command
def OpenCom():
    Info.ACCESS = ACCTEXT.get_access_text("open")

    GetCommand()

    file_path = os.path.join(Info.folder_path, command)

    if os.path.exists(file_path):
        Info.FileName, FileExtension = os.path.splitext(command)

        set_filename(Info.FileName)

        if FileExtension == ".json":
            Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)
            LineUI()
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Success!{bcolors.ENDC} your file {bcolors.PURPLE}{Info.FileName}.json{bcolors.ENDC} has been opened successfully')
            LineUI()
        else:
            WrongFile()
            return
        
    else:
        if command == "/exit":
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return
        
        else:
            DirNotFound()
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return

    GetCommand()

    while command != "/exit":
        if command == "/exit":
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return

        else:
            UnkCom()

        GetCommand()


    Info.ACCESS = ACCTEXT.get_access_text("default")
    return


# Import Command Help
def OpenHelpCom():
    LineUI()
    print(f'To use the {bcolors.OKCYAN}/open{bcolors.ENDC}, simply enter the {bcolors.PURPLE}Open Mode{bcolors.ENDC} and add the name of the file you want to open.')
    print(f'For Example : ')
    print(f'{bcolors.PURPLE}/open')
    print(f'{bcolors.PURPLE}default.json{bcolors.ENDC}')
    LineUI()


# Create Command
# Create Command
def CreateCom():
    Info.ACCESS = ACCTEXT.get_access_text("create")

    GetCommand()

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
            LineUI()
            print(f'{bcolors.OKGREEN}Notice:{bcolors.ENDC} Created missing folder {bcolors.PURPLE}{Info.folder_path}{bcolors.ENDC}')
        except PermissionError:
            LineUI()
            print(f'{bcolors.WARNING}Error: Cannot create folder {bcolors.PURPLE}{Info.folder_path}{bcolors.WARNING} due to permission issues.{bcolors.ENDC}')
            Info.ACCESS = ACCTEXT.get_access_text("default")
            return

    if os.path.exists(file_path):
        LineUI()
        print(f'{bcolors.WARNING}Error: The file {bcolors.PURPLE}{Info.FileName}.json{bcolors.WARNING} already exists.{bcolors.ENDC}')
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    try:
        with open(file_path, 'w') as json_file:
            json.dump({}, json_file)
        LineUI()
        print(f'{bcolors.OKGREEN}{bcolors.BOLD}Success!{bcolors.ENDC} Your file {bcolors.PURPLE}{Info.FileName}.json{bcolors.ENDC} was successfully created')
        LineUI()
    except PermissionError:
        LineUI()
        print(f'{bcolors.WARNING}Error: Cannot create file {bcolors.PURPLE}{Info.FileName}.json{bcolors.WARNING} due to permission issues.{bcolors.ENDC}')
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    while True:
        GetCommand()
        if command == "/exit":
            break
        else:
            UnkCom()

    Info.ACCESS = ACCTEXT.get_access_text("default")


# Purge Command
def PurgeCom():
    Info.ACCESS = ACCTEXT.get_access_text("purge")

    GetCommand()

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
        DirNotFound()
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.FileName, FileExtension = os.path.splitext(command)
    set_filename(Info.FileName)

    if FileExtension != ".json":
        ErrNoPerm()
        Info.ACCESS = ACCTEXT.get_access_text("default")
        return

    Info.ACCESS = ACCTEXT.get_access_text("filedelete", Info.FileName)
    VerifyCom()

    GetCommand()
    if command == "YES":
        try:
            os.remove(file_path)
            LineUI()
            print(f'{bcolors.OKGREEN}{bcolors.BOLD}Success!{bcolors.ENDC} The file {bcolors.PURPLE}{Info.FileName}.json{bcolors.ENDC} has been deleted')
            LineUI()

            Info.ACCESS = ACCTEXT.get_access_text("default")

            return
        
        except PermissionError:
            LineUI()
            print(f'{bcolors.WARNING}Error: Cannot delete file {bcolors.PURPLE}{Info.FileName}.json{bcolors.WARNING} due to permission issues.{bcolors.ENDC}')
    else:
        LineUI()
        print(f'{bcolors.WARNING}Purge canceled.{bcolors.ENDC}')
        LineUI()

    while True:
        GetCommand()
        if command == "/exit":
            break
        else:
            UnkCom()

    Info.ACCESS = ACCTEXT.get_access_text("default")


# Import Command Help
def CreateHelpCom():
    LineUI()
    print(f'To use the {bcolors.OKCYAN}/create{bcolors.ENDC}, simply enter the {bcolors.PURPLE}Create Mode{bcolors.ENDC} and add the name of the file you want to create.')
    print(f'For Example : ')
    print(f'{bcolors.PURPLE}/create')

    print(f'{bcolors.PURPLE}default.json{bcolors.ENDC}')
    LineUI()

# Frequently Accessible Functions
def GetCommand():
    global command
    command = input(f'{Info.ACCESS}')


# Error Handling
def VerifyCom():
    LineUI()
    print(f'To purge the file {bcolors.OKCYAN}{Info.FileName}{bcolors.ENDC}, simply write {bcolors.PURPLE}{bcolors.BOLD}<YES>{bcolors.ENDC}. Writing anything else would cancel the action with an error')
    LineUI()

def UnkCom():
    LineUI()
    print(bcolors.WARNING + "Error: The Command You Provided Is Not Valid!" + bcolors.ENDC)
    print("To Get A List Of Valid Commands, Try: (Remember to check the mode you have entered)")
    print(bcolors.OKCYAN + "/commands" + bcolors.ENDC + "       | Displays a list of the commands available")
    LineUI()


def UnkComCom():
    LineUI()
    print(bcolors.WARNING + "Error: The Command You Provided Is Not Valid!" + bcolors.ENDC)
    print("Try One Of These Commands: ")
    print(bcolors.OKCYAN + "/next" + bcolors.ENDC + "       | Goes to the next page of the Commands List")
    print(bcolors.OKCYAN + "/prev" + bcolors.ENDC + "       | Goes to the previous page of the Commands List")
    print(bcolors.OKCYAN + "/exit" + bcolors.ENDC + "       | Exits The Commands Display Mode")
    LineUI()


def DirNotFound():
    LineUI()
    print(f'{bcolors.WARNING}Error: The File You Provided Is Not Valid/Found. Remember to add the {bcolors.PURPLE}.json{bcolors.ENDC}{bcolors.WARNING} extension!{bcolors.ENDC}')
    LineUI()


def WrongFile():
    LineUI()
    print(f'{bcolors.WARNING}Error: The File {bcolors.PURPLE}{Info.FileName}{bcolors.WARNING} You Provided Is Not A Valid File Type (Accepts Only .json)!{bcolors.ENDC}')
    LineUI()


def ErrMaxPage():
    LineUI()
    print(f'{bcolors.WARNING}There are not any pages left!{bcolors.ENDC}')
    LineUI()


def ErrMinPage():
    LineUI()
    print(f'{bcolors.WARNING}There are not any pages left!{bcolors.ENDC}')
    LineUI()

def ErrNoPerm():
    LineUI()
    print(f'{bcolors.WARNING}The request has been blocked (No Permission Given){bcolors.ENDC}')
    LineUI()

# Main Function
def Main(CurrentPage):    
    StartManager()
    HelpCom()

    GetCommand()

    while command != "/quit":
        
        if command == "/quit":
            quit()
        elif command == "/about":
            AboutCom()
        elif command == "/help":
            HelpCom()
        elif command == "/commands":
            Info.ACCESS = ACCTEXT.get_access_text("commands")
            ComCom(CurrentPage)

            GetCommand()

            while command != "/exit":
                
                if command == "/next" and CurrentPage < MaxPage:
                    CurrentPage += 1
                    ComCom(CurrentPage)

                elif command == "/next" and CurrentPage == MaxPage:
                    ErrMaxPage()

                elif command == "/prev" and CurrentPage > 1:
                    CurrentPage -= 1
                    ComCom(CurrentPage)

                elif command == "/prev" and CurrentPage == 1:
                    ErrMinPage()

                elif command == "/open":
                    OpenHelpCom()

                elif command == "/create":
                    CreateHelpCom()

                elif command == "/exit":
                    break 

                else:
                    UnkComCom()

                GetCommand()

            Info.ACCESS = ACCTEXT.get_access_text("default")

        elif command == "/open":
            OpenCom()
        elif command == "/create":
            CreateCom()
        elif command == "/purge":
            PurgeCom()
        else:
            UnkCom()

        GetCommand()

if __name__ == "__main__":
    Main(Info.CurrentPage)