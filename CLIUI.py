from data import bcolors, Info

# Standard UI Line Draw
def LineUI():
    print("=" * 70)


# Horizontal Logo Draw
def LogoDraw():
    for i in Logo.HorVersion:
        print(i)


# Welcome Message
def welcome_message():
    LineUI()
    print("Welcome To Creative Tools - Electronics Inventory Manager")
    print(f'Developed By Rafail Palalakis, Version : {bcolors.PURPLE}{Info.VERSION}{bcolors.ENDC}')
    print("To Get Started Try One Of These Commands Below:")
    LineUI()


# UI Data
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