import os

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
    VERSION = "1.4Dev"
    DATE = "18/12/2025 (1st Commit Of The Day)"
    ACCESSNAME = "System"
    ACCESS = f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESSNAME}){bcolors.ENDC} -> "
    CurrentPage = 1
    FileName: int


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
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}{bcolors.ENDC}{bcolors.OKGREEN}>Purge{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
        elif mode == "filedelete":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Purge{bcolors.ENDC}) -> "
        elif mode == "mode-com":
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{bcolors.OKGREEN}{filename}{bcolors.ENDC}{bcolors.OKGREEN}>Commands{bcolors.ENDC}) -> "
        else:
            return f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{Info.ACCESSNAME}){bcolors.ENDC} -> "


# Commands List
class COMMANDSLIST:
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

# Logo
class Logo:
    HorVersion = [
        "    ________          __                   _          ",
        "   ╱ ____╱ ╱__  _____╱ ╱__________  ____  (_)_________",
        "  ╱ __╱ ╱ ╱ _ ╲╱ ___╱ __╱ ___╱ __ ╲╱ __ ╲╱ ╱ ___╱ ___╱",
        " ╱ ╱___╱ ╱  __╱ ╱__╱ ╱_╱ ╱  ╱ ╱_╱ ╱ ╱ ╱ ╱ ╱__(__  )   ",
        "╱_____╱_╱╲___╱╲___╱╲__╱_╱   ╲____╱_╱ ╱_╱_╱╲___╱____╱  ",
        "      ╱  _╱___ _   _____  ____  ╱ ╱_____  _______  __ ",
        "      ╱ ╱╱ __ ╲ │ ╱ ╱ _ ╲╱ __ ╲╱ __╱ __ ╲╱ ___╱ ╱ ╱ ╱ ",
        "    _╱ ╱╱ ╱ ╱ ╱ │╱ ╱  __╱ ╱ ╱ ╱ ╱_╱ ╱_╱ ╱ ╱  ╱ ╱_╱ ╱  ",
        "   ╱___╱_╱ ╱_╱│___╱╲___╱_╱ ╱_╱╲__╱╲____╱_╱   ╲__, ╱   ",
        "      ╱  │╱  ╱___ _____  ____ _____ ____  __╱____╱    ",
        "     ╱ ╱│_╱ ╱ __ `╱ __ ╲╱ __ `╱ __ `╱ _ ╲╱ ___╱       ",
        "    ╱ ╱  ╱ ╱ ╱_╱ ╱ ╱ ╱ ╱ ╱_╱ ╱ ╱_╱ ╱  __╱ ╱           ",
        "   ╱_╱  ╱_╱╲__,_╱_╱ ╱_╱╲__,_╱╲__, ╱╲___╱_╱            ",
        "                            ╱____╱                    ",
    ]


# Frequently Accessible Functions
def set_filename(filename):
    Info.FileName = filename
    # Update ACCESS dynamically after changing the filename
    Info.ACCESS = ACCTEXT.get_access_text("file", Info.FileName)