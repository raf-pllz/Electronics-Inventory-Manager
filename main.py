# Constants
VERSION = "1.0Dev"
DATE = "16/12/2025"


# Defaults
ACCESS = "Undefined"


# ASCII Coloring
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


# Structures
Commands = {
    'bcolors.OKCYAN + "/about" + bcolors.ENDC + "          | Displays a list of information about this software"',
    'bcolors.OKCYAN + "/commands" + bcolors.ENDC + "       | Displays a list of the commands available"',
    'bcolors.OKCYAN + "/help" + bcolors.ENDC + "           | Gives a list of the most important/useful commands"',
    'bcolors.OKCYAN + "/quit" + bcolors.ENDC + "           | Quits and closes the terminal window"',
}


# Launch Process
def StartManager():
    LineUI()
    print ("Welcome To Creative Tools - Electronics Inventory Manager")
    print(f'Developed By Rafail Palalakis, Version : {bcolors.PURPLE}{VERSION}{bcolors.ENDC}')
    print ("To Get Started Try One Of These Commands Bellow:")
    

# Commands List
def HelpCom():   
    LineUI()
    print (f'{bcolors.OKCYAN}/help{bcolors.ENDC}             | Gives a list of the most important/useful commands')
    print (f'{bcolors.OKCYAN}/quit{bcolors.ENDC}             | Quits and closes the terminal window')
    print (f'{bcolors.OKCYAN}/help{bcolors.ENDC}             | Gives a list of the most important/useful commands')
    print (f'{bcolors.OKCYAN}/about{bcolors.ENDC}            | Displays a list of information about this software')
    LineUI()

def AboutCom():
    LineUI()
    print ("Creative Tools - Electronics Inventory Manager")
    print (f'Software Version : {bcolors.PURPLE}{VERSION}{bcolors.ENDC}')
    print (f'Release Date : {bcolors.PURPLE}{DATE}{bcolors.ENDC}')
    print ("© 2025, Made By Rafail Palalakis, All Rights Reserved")
    print ("Built with ❤️  using Python 3")
    print ("My LinkedIn Page : https://www.linkedin.com/in/raf-pllz/")
    LineUI()

def ComCom():
    LineUI()
    print("The Complete List Of Commands : ")
    

# Frequently Accessible Functions
def GetCommand():
    global command
    command = input(f'({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESS}){bcolors.ENDC} -> ')

# Error Handling
def UnkCom():
    LineUI()
    print (bcolors.WARNING + "Error : The Command You Provided Is Not Valid/Found!" + bcolors.ENDC)
    print ("To Get A List Of Commands, Try : ")
    print (bcolors.OKCYAN + "/commands" + bcolors.ENDC + "       | Displays a list of the commands available")
    LineUI()


# UI Decorations
def LineUI():
    print ("====================================================================")

#Main Part Of The Code
StartManager()
HelpCom()

#Read The Command Given By The User
GetCommand()

while (command != "/quit"):

    # Command (/info)
    if command == "/quit":
        quit()
    elif command == "/about":
        AboutCom()
    elif command =="/help":
        HelpCom()
    else:
        UnkCom()

    # Ask For Command Before The End Of The Loop
    GetCommand()