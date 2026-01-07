import getpass

from dataclasses import dataclass
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    PURPLE = '\033[0;35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Defaults
class Info:
    CurrentPage = 1
    folder_path = "./Databases"
    VERSION = "1.5.1Dev"
    DATE = "07/1/2026 (1st Commit Of The Day)"
    ACCESSNAME = getpass.getuser()
    ACCESS = f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESSNAME}){bcolors.ENDC} -> "
    CurrentPage = 1
    FileName = "none"


    # About Page Strings
    AboutStrings = [
        f'Software Version : {bcolors.PURPLE}{VERSION}{bcolors.ENDC}',
        f'Release Date : {bcolors.PURPLE}{DATE}{bcolors.ENDC}',
        f'© 2026, Made By Rafail Palalakis, All Rights Reserved',
        f'Built with ❤️  using {bcolors.PURPLE}Python 3{bcolors.ENDC}',
        f'My LinkedIn Page : {bcolors.OKBLUE}https://www.linkedin.com/in/raf-pllz/{bcolors.ENDC}',
        f'The Project\'s GitHub Repository : {bcolors.OKBLUE}https://github.com/raf-pllz/Electronics-Inventory-Manager{bcolors.ENDC}',
    ]


    # Help Page Strings
    HelpStrings = [
        f'{bcolors.OKCYAN}/help{bcolors.ENDC}             | Gives a list of the most important/useful commands',
        f'{bcolors.OKCYAN}/quit{bcolors.ENDC}             | Quits and closes the terminal window',
        f'{bcolors.OKCYAN}/about{bcolors.ENDC}            | Displays a list of information about this software',
        f'{bcolors.OKCYAN}/commands{bcolors.ENDC}         | Displays a list of the commands available'
    ]


    # Open Command Help Page Strings
    OpenCommandHelpStrings = [
        f"{bcolors.HEADER}{bcolors.BOLD}Open Command Guide{bcolors.ENDC}",
        "",
        f"{bcolors.OKCYAN}/open{bcolors.ENDC}  | Load an existing {bcolors.PURPLE}.json{bcolors.ENDC} inventory file from the {bcolors.OKBLUE}{bcolors.BOLD}Vault Directory{bcolors.ENDC}.",
        "",
        f"{bcolors.OKGREEN}{bcolors.BOLD}Usage Format:{bcolors.ENDC}",
        f"  {bcolors.OKCYAN}/open{bcolors.ENDC}",
        f"  {bcolors.PURPLE}filename.json{bcolors.ENDC}",
        "",
        f"{bcolors.WARNING}{bcolors.BOLD}Abort / Exit:{bcolors.ENDC}",
        f"  - When prompted for a file name, type {bcolors.FAIL}/exit{bcolors.ENDC} to cancel and return to {bcolors.OKBLUE}default terminal mode{bcolors.ENDC}.",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Validation Rules:{bcolors.ENDC}",
        f"  - Only {bcolors.PURPLE}.json{bcolors.ENDC} files are accepted.",
        f"  - Non-JSON extensions trigger an {bcolors.FAIL}Error : Wrong File{bcolors.ENDC}.",
        f"  - Unknown file names trigger an {bcolors.FAIL}Error : Directory Not Found{bcolors.ENDC}.",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Post-Load Capabilities:{bcolors.ENDC}",
        f"  - Once a file is opened, inventory actions {bcolors.OKGREEN}/add{bcolors.ENDC} and {bcolors.FAIL}/remove{bcolors.ENDC} become available.",
    ]


    # Create Command Help Page Strings
    CreateCommandHelpStrings = [
        f"{bcolors.HEADER}{bcolors.BOLD}Create Command Guide{bcolors.ENDC}",
        "",
        f"{bcolors.OKCYAN}/create{bcolors.ENDC}  | Create a new {bcolors.PURPLE}.json{bcolors.ENDC} file inside the {bcolors.OKBLUE}{bcolors.BOLD}Vault Directory{bcolors.ENDC}.",
        "",
        f"{bcolors.OKGREEN}{bcolors.BOLD}Usage Format:{bcolors.ENDC}",
        f"  {bcolors.OKCYAN}/create{bcolors.ENDC}",
        f"  {bcolors.PURPLE}filename{bcolors.ENDC}  {bcolors.BOLD}(extension optional){bcolors.ENDC}",
        "",
        f"{bcolors.WARNING}{bcolors.BOLD}Abort / Exit:{bcolors.ENDC}",
        f"  - When prompted for a file name, type {bcolors.FAIL}/exit{bcolors.ENDC} to cancel and return to {bcolors.OKBLUE}default terminal mode{bcolors.ENDC}.",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}File Creation Rules:{bcolors.ENDC}",
        f"  - If the Vault directory does not exist, it is auto-created before file generation.",
        f"  - Existing file names trigger {bcolors.FAIL}Error : File Already Exists{bcolors.ENDC}.",
        f"  - Permission issues trigger {bcolors.FAIL}Error : No Permission{bcolors.ENDC}.",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Post-Create Behavior:{bcolors.ENDC}",
        f"  - After creation, the file automatically opens in {bcolors.OKBLUE}{bcolors.BOLD}File Mode{bcolors.ENDC}.",
        f"  - Once inside File Mode, commands like {bcolors.OKGREEN}/add{bcolors.ENDC} and {bcolors.FAIL}/remove{bcolors.ENDC} become available.",
]
    
    # Purge Command Help Page Strings
    PurgeCommandHelpStrings = [
        f"{bcolors.HEADER}{bcolors.BOLD}Purge Command Guide{bcolors.ENDC}",
        "",
        f"{bcolors.OKCYAN}/purge{bcolors.ENDC}  | Delete an existing {bcolors.PURPLE}.json{bcolors.ENDC} file from the {bcolors.OKBLUE}{bcolors.BOLD}Vault Directory{bcolors.ENDC}.",
        "",
        f"{bcolors.OKGREEN}{bcolors.BOLD}Usage Format :{bcolors.ENDC}",
        f"  {bcolors.OKCYAN}/purge{bcolors.ENDC}",
        f"  {bcolors.PURPLE}default.json{bcolors.ENDC}",
        f"  {bcolors.OKGREEN}{bcolors.BOLD}YES{bcolors.ENDC}",
        "",
        f"{bcolors.WARNING}{bcolors.BOLD}Abort / Cancel:{bcolors.ENDC}",
        f"  - Type {bcolors.FAIL}/exit{bcolors.ENDC} anytime to cancel and return to {bcolors.OKBLUE}default terminal mode{bcolors.ENDC}",
        f"  - Any invalid input during confirmation cancels the purge process",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Validation Rules:{bcolors.ENDC}",
        f"  - Only {bcolors.PURPLE}.json{bcolors.ENDC} files can be purged",
        f"  - Missing Vault directory triggers {bcolors.WARNING}Error: Database folder does not exist{bcolors.ENDC}",
        f"  - Unknown file name triggers {bcolors.FAIL}Error: Directory Not Found{bcolors.ENDC}",
        f"  - Permission issues trigger {bcolors.FAIL}Error: No Permission{bcolors.ENDC}",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Expected System Messages:{bcolors.ENDC}",
        f"  - Verify prompt appears before deletion confirmation",
        f"  - Success message returns {bcolors.OKCYAN}/exit{bcolors.ENDC} access state to default after purge",
    ]

    # Notes Command Strings
    DevNotes = [
        f"{bcolors.HEADER}{bcolors.BOLD}Changelog — Electronics Inventory Manager{bcolors.ENDC}",
        "",
        f"{bcolors.PURPLE}{bcolors.BOLD}Current Update [1.5.1Dev] — 07/01/2026{bcolors.ENDC}",
        "",
        f"{bcolors.OKGREEN}{bcolors.BOLD}Added:{bcolors.ENDC}",
        "- /notes command for quick access to latest changes",
        "- CLI prompt tag updated from '@system' to actual computer username",
        "- Mode-aware help string arrays for /open, /create, /purge",
        "",
        f"{bcolors.OKCYAN}{bcolors.BOLD}Refactored Framework:{bcolors.ENDC}",
        "- main logic split into modular scripts (commands, notifications, UI, JSON processing)",
        "- Shared state centralized in data.py",
        "- Debug and development workflow improved",
        "",
        f"{bcolors.FAIL}{bcolors.BOLD}Warranty:{bcolors.ENDC}",
        "This software is provided 'as-is' with no guarantees during development builds.",
        "Always keep backups of your inventory files.",
        "",
        "© 2026 Rafail Palalakis. All rights reserved.",
    ]


# ACCESS TEXT (dynamic generation based on mode)
class ACCTEXT:
    @staticmethod
    def get_access_text(mode, filename=None):
        if mode == "default":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}){bcolors.ENDC} -> "
        elif mode == "commands":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}{bcolors.ENDC}{bcolors.OKGREEN}>Commands{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
        elif mode == "file" and filename:
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}) -> "
        elif mode == "open":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}{bcolors.ENDC}{bcolors.OKGREEN}>Open{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
        elif mode == "create":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}{bcolors.ENDC}{bcolors.OKGREEN}>Create{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
        
        elif mode == "purge":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}{bcolors.ENDC}{bcolors.FAIL}>Purge{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
        elif mode == "filedelete":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.FAIL}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Purge{bcolors.ENDC}) -> "
        
        elif mode == "mode-com":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Commands{bcolors.ENDC}) -> "
        elif mode == "add-name":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Add>Name{bcolors.ENDC}) -> "
        elif mode == "add-desc":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Add>Description{bcolors.ENDC}) -> "
        elif mode == "add-stock":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Add>Stock{bcolors.ENDC}) -> "
        elif mode == "add-id":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Add>ID{bcolors.ENDC}) -> "
        
        # Mode : Remove/Delete Object From .json File
        elif mode == "remove":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.FAIL}>Remove{bcolors.ENDC}) -> "
        
        # Mode : Remove/Delete Object From .json File (With ID)
        elif mode == "remove-id":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.FAIL}>Remove>ID{bcolors.ENDC}) -> "
        
        # Mode : Remove/Delete Object From .json File (With NAME)
        elif mode == "remove-name":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.FAIL}>Remove>Name{bcolors.ENDC}) -> "
        
        # Default Handling
        else:
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}){bcolors.ENDC} -> "


# Commands List
class COMMANDSLIST:
    # List of Commands
    Commands = [
        f"{bcolors.OKCYAN}/about{bcolors.ENDC}                | Displays a list of information about this software",
        f"{bcolors.OKCYAN}/notes{bcolors.ENDC}                | Displays all the latest changes in the current version"
        f"{bcolors.OKCYAN}/commands{bcolors.ENDC}             | Displays a list of the commands available",
        f"{bcolors.OKCYAN}|- /ANYCOMMAND{bcolors.ENDC}        | Write any command to get help on how to use it",
        f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}              | Exits The Commands Display Mode\n",

        f"{bcolors.OKCYAN}/help{bcolors.ENDC}                 | Gives a list of the most important/useful commands",
        f"{bcolors.OKCYAN}/quit{bcolors.ENDC}                 | Quits and closes the terminal window",
        f"{bcolors.OKCYAN}/open{bcolors.ENDC}                 | Opens a (.json) file in the Vault Directory",
        f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}              | Exits The Open Mode\n",

        f"{bcolors.OKCYAN}/create{bcolors.ENDC}               | Creates a (.json) file in the Vault Directory",
        f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}             | Exits The Create Mode\n",

        f"{bcolors.OKCYAN}/purge{bcolors.ENDC}               | Remove a (.json) file from the Vault Directory",
        f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}             | Exits The Purge Mode\n",

        f"{bcolors.OKCYAN}ANYFILE{bcolors.ENDC}              | When being in any file",
        f"{bcolors.OKCYAN}|- /add{bcolors.ENDC}              | Add An Object To The Current (.json) File",
        f"{bcolors.OKCYAN}|- /remove{bcolors.ENDC}           | Remove An Object To The Current (.json) File",
        f"{bcolors.OKCYAN}|- /commands{bcolors.ENDC}           | Displays a list of the commands available",
        f"{bcolors.OKCYAN}|-- /ANYCOMMAND{bcolors.ENDC}        | Write any command to get help on how to use it",
        f"{bcolors.OKCYAN}|-- /exit{bcolors.ENDC}              | Exits The Commands Display Mode\n",
]


@dataclass
class Component:
    name: str
    description: str
    stock: int
    id : int


# Function to set ObjName
def set_ObjName(comp: Component, ObjName):
    comp.name = ObjName


# Function to set ObjDescription
def set_ObjDescription(comp: Component, ObjDescription):
    comp.description = ObjDescription


# Function to set ObjStock
def set_ObjStock(comp : Component, ObjStock):
    comp.stock = ObjStock


# Function to set ObjStock
def set_ObjID(comp : Component, ObjID):
    comp.id = ObjID


def component_to_dict(comp: Component) -> dict:
    d = {
        "obj_name": comp.name,
        "obj_description": comp.description,
        "obj_stock": comp.stock,  
        "obj_id": comp.id,
    }
    
    return d

# Frequently Accessible Functions
def set_filename(filename):
    Info.FileName = filename
    Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)