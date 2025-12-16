# Constants
VERSION = "1.1Dev"
DATE = "16/12/2025 (2st Commit Of The Day)"

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


# Defaults
ACCESSNAME = "Undefined"
ACCESS = f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESSNAME}){bcolors.ENDC} -> "

global CurrentPage
CurrentPage = 1


# List of Commands
Commands = [
    f"{bcolors.OKCYAN}/about{bcolors.ENDC}          | Displays a list of information about this software",
    f"{bcolors.OKCYAN}/commands{bcolors.ENDC}       | Displays a list of the commands available",
    f"{bcolors.OKCYAN}/exit{bcolors.ENDC}           | Exits The Commands Display Mode",
    f"{bcolors.OKCYAN}|- /exit{bcolors.ENDC}        | Exits The Commands Display Mode\n",
    f"{bcolors.OKCYAN}/help{bcolors.ENDC}           | Gives a list of the most important/useful commands",
    f"{bcolors.OKCYAN}/quit{bcolors.ENDC}           | Quits and closes the terminal window",
]

MaxPage = (len(Commands) + 9) // 10 


# UI Decorations
def LineUI():
    print("=" * 70)

# Launch Process
def StartManager():
    LineUI()
    print("Welcome To Creative Tools - Electronics Inventory Manager")
    print(f'Developed By Rafail Palalakis, Version : {bcolors.PURPLE}{VERSION}{bcolors.ENDC}')
    print("To Get Started Try One Of These Commands Below:")

# Commands List
def HelpCom():   
    LineUI()
    print(f'{bcolors.OKCYAN}/help{bcolors.ENDC}             | Gives a list of the most important/useful commands')
    print(f'{bcolors.OKCYAN}/quit{bcolors.ENDC}             | Quits and closes the terminal window')
    print(f'{bcolors.OKCYAN}/about{bcolors.ENDC}            | Displays a list of information about this software')
    print(f'{bcolors.OKCYAN}/commands{bcolors.ENDC}         | Displays a list of the commands available')
    LineUI()

def AboutCom():
    LineUI()
    print("Creative Tools - Electronics Inventory Manager")
    print(f'Software Version : {bcolors.PURPLE}{VERSION}{bcolors.ENDC}')
    print(f'Release Date : {bcolors.PURPLE}{DATE}{bcolors.ENDC}')
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

    print(f'Page ({bcolors.BOLD}{CurrentPage}/{MaxPage}{bcolors.ENDC})')
    LineUI()

# Frequently Accessible Functions
def GetCommand():
    global command
    command = input(f'{ACCESS}')


def UnkCom():
    LineUI()
    print(bcolors.WARNING + "Error: The Command You Provided Is Not Valid/Found!" + bcolors.ENDC)
    print("To Get A List Of Commands, Try: ")
    print(bcolors.OKCYAN + "/commands" + bcolors.ENDC + "       | Displays a list of the commands available")
    LineUI()

def UnkComCom():
    LineUI()
    print(bcolors.WARNING + "Error: The Command You Provided Is Not Valid/Found!" + bcolors.ENDC)
    print("Try One Of These Commands: ")
    print(bcolors.OKCYAN + "/next" + bcolors.ENDC + "       | Goes to the next page of the Commands List")
    print(bcolors.OKCYAN + "/prev" + bcolors.ENDC + "       | Goes to the previous page of the Commands List")
    print(bcolors.OKCYAN + "/exit" + bcolors.ENDC + "       | Exits The Commands Display Mode")
    LineUI()


# Main Function
def Main():
    global CurrentPage, ACCESS
    
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
            ACCESS = f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESSNAME}{bcolors.ENDC}{bcolors.OKGREEN}>Commands{bcolors.ENDC}{bcolors.BOLD}){bcolors.ENDC} -> "
            ComCom(CurrentPage)

            GetCommand()

            while command != "/exit":
                
                if command == "/next" and CurrentPage < MaxPage:
                    CurrentPage += 1
                    ComCom(CurrentPage)

                elif command == "/prev" and CurrentPage > 1:
                    CurrentPage -= 1
                    ComCom(CurrentPage)
                    
                elif command == "/exit":
                    break 
                else:
                    UnkComCom()

                GetCommand()

            ACCESS = f"({bcolors.OKBLUE}@{bcolors.ENDC}{bcolors.BOLD}{ACCESSNAME}){bcolors.ENDC} -> "

        else:
            UnkCom()

        # Ask For Command Before The End Of The Loop
        GetCommand()

# Start the main function
if __name__ == "__main__":
    Main()