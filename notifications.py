from CLIUI import LineUI
from data import bcolors

# Added Object To Vault Success Message
def obj_add_success(ObjName, FileName):
    LineUI()
    print(f'{bcolors.OKGREEN}{bcolors.BOLD}Success!{bcolors.ENDC} your object {bcolors.PURPLE}{ObjName}{bcolors.ENDC} has been added to {bcolors.PURPLE}{FileName}.json{bcolors.ENDC} successfully')
    LineUI()


# Removed Object To Vault Success Message
def obj_remove_success(ObjName, FileName):
    LineUI()
    print(f'{bcolors.OKGREEN}{bcolors.BOLD}Success!{bcolors.ENDC} your object {bcolors.PURPLE}{ObjName}{bcolors.ENDC} has been removed from {bcolors.PURPLE}{FileName}.json{bcolors.ENDC} successfully')
    LineUI()