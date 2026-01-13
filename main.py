from data import Info, ACCTEXT
from jsonprocess import create_default_database
from notifications import NotificationCall
from CLIUI import welcome_message
from commands import GetCommand, AboutCommand, HelpCommand, ComCom, OpenCommand, CreateCommand, PurgeCommand, ReleaseNotes


# Launch Process
def StartManager():
    create_default_database()
    welcome_message(Info.VERSION)


# Main Function
def Main():    
    StartManager()
    HelpCommand()

    command = GetCommand()

    while command != "/quit":
        
        if command == "/quit":
            quit()
        elif command == "/about":
            AboutCommand()
        elif command == "/help":
            HelpCommand()
        elif command == "/commands":
            Info.ACCESS = ACCTEXT.get_access_text("commands")
            ComCom(Info.CurrentPage)

            Info.ACCESS = ACCTEXT.get_access_text("default")

        elif command == "/open":
            OpenCommand(Info.CurrentPage)
        elif command == "/create":
            CreateCommand(Info.CurrentPage)
        elif command == "/purge":
            PurgeCommand()
        elif command == "/notes":
            ReleaseNotes()
        else:
            MsgMode = "error-unknown-command"
            NotificationCall(MsgMode, Info.FileName)

        command = GetCommand()


if __name__ == "__main__":
    Main()