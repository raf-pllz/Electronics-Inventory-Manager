from CLIUI import LineUI
from data import Info, bcolors


# Initiate Notification Call
def NotificationCall(mode, filename):
    LineUI()
    print(f'{ErrorMSG(mode, filename)}')
    LineUI()

# Get Correct Value
def GetCorrectValue(value):
    global correctvalue
    correctvalue = value

# Ger Directory As String
def GetDirectory(value):
    global directory
    directory = value

# Get Notification Modes
def ErrorMSG(mode, filename):
    WarningTXT = (f"{bcolors.FAIL}Warning!{bcolors.ENDC}")
    ErrorTXT = (f"{bcolors.WARNING}Error!{bcolors.ENDC}")
    SuccessTXT = (f"{bcolors.PURPLE}Success!{bcolors.ENDC}")
    VerifyTXT = (f"{bcolors.PURPLE}Verify!{bcolors.ENDC}")
    NoticeTXT = (f"{bcolors.OKBLUE}Notice!{bcolors.ENDC}")

    # Pages (Min/Max)
    if mode == "error-max-page":
        return f"{ErrorTXT} You have reached the end of the page. Go back by using {bcolors.PURPLE}/prev{bcolors.ENDC}"
    elif mode == "error-min-page":
        return f"{ErrorTXT} There are not any pages back there. Go to the next page by using {bcolors.PURPLE}/next{bcolors.ENDC}"
    
    # Errors
    elif mode == "error-unknown-command":
        return f"{ErrorTXT} The Command You Provided Is Not Valid\nTo Get A List Of Valid Commands, Try: (Remember to check the mode you have entered)\n{bcolors.OKCYAN}/commands{bcolors.ENDC}       | Displays a list of the commands available"
    elif mode == "error-unknown-command-command":
        return f"{ErrorTXT} The Command You Provided Is Not Valid!\nTry One Of These Commands Bellow :\n{bcolors.OKCYAN}/next{bcolors.ENDC}       | Goes to the next page of the Commands List\n{bcolors.OKCYAN}/prev{bcolors.ENDC}       | Goes to the previous page of the Commands List\n{bcolors.OKCYAN}/exit{bcolors.ENDC}       | Exits The Commands Display Mode"
    elif mode == "error-invalid-value":

        return f"{ErrorTXT} The value you have entered is not correct, it should be {bcolors.OKGREEN}{correctvalue}{bcolors.ENDC}"
    elif mode == "error-invalid-obj":
        return f"{ErrorTXT} The value you have entered is not correct"
    elif mode == "error-no-permission":
        return f"{ErrorTXT} Cannot complete action due to permission settings"
    elif mode == "error-directory-not-found":
        return f"{ErrorTXT} The File You Provided Is Not Valid/Found. Remember to add the {bcolors.PURPLE}.json{bcolors.ENDC}{bcolors.WARNING} extension!{bcolors.ENDC}"
    elif mode == "error-file-already-exists":
        return f"{ErrorTXT} The file {bcolors.PURPLE}{filename}{bcolors.ENDC}{bcolors.FAIL}already exists{bcolors.ENDC}"
    elif mode == "error-wrong-file":
        return f"{ErrorTXT} The File {bcolors.PURPLE}{Info.FileName}{bcolors.WARNING} You Provided Is Not A Valid File Type (Accepts Only .json)!{bcolors.ENDC}"
    
    # Successes
    elif mode == "success-obj-add":
        return f"{SuccessTXT} The object {bcolors.PURPLE}{filename}{bcolors.ENDC} has been saved to {bcolors.PURPLE}{directory}{bcolors.ENDC}"
    elif mode == "success-obj-remove":
        return f"{SuccessTXT} The object {bcolors.PURPLE}{filename}{bcolors.ENDC} has been removed from {bcolors.PURPLE}{directory}{bcolors.ENDC}"
    elif mode == "success-file-purge":
        return f"{SuccessTXT} The file {bcolors.PURPLE}{filename}{bcolors.ENDC} has been {bcolors.FAIL}deleted{bcolors.ENDC}"
    elif mode == "success-file-add":
        return f"{SuccessTXT} The file {bcolors.PURPLE}{filename}{bcolors.ENDC} has been {bcolors.OKGREEN}created{bcolors.ENDC}"
    elif mode == "success-file-open":
        return f"{SuccessTXT} The file {bcolors.PURPLE}{filename}{bcolors.ENDC} has been {bcolors.OKGREEN}opened{bcolors.ENDC}"
    
    # Verifications
    elif mode == "verify-command":
        return f"{VerifyTXT} To proceed, please confirm by entering{bcolors.PURPLE}<YES>{bcolors.ENDC}"
    
    # Notifications
    elif mode == "notice-purge-canceled":
        return f"{NoticeTXT} Purge has been {bcolors.FAIL}canceled{bcolors.ENDC}"
    elif mode == "notice-directory-added":
        return f"{NoticeTXT} Directory folder has been {bcolors.OKGREEN}created{bcolors.ENDC}"
    elif mode == "notifce-default-directory-created":
        return f"{NoticeTXT} Performed a {bcolors.PURPLE}Database{bcolors.ENDC} vault/folder creation (as there wasn\'t any other present)"