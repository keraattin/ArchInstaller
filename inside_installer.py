#!usr/bin/env python3

import os
import sys

#Colors
DEFAULT = "\33[37m"
GREEN = "\33[32m"
RED = "\33[31m"
CYAN = "\33[36m"
MAGENTA = "\33[35m"

#User Informations
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""

#Setting new password for root
def set_root_password():
    os.system("clear")
    root_password = input("\nPlease enter the root password : ")
    repeat_root_password = input("\nRoot password again : ")
    if root_password == repeat_root_password:
        os.system("echo -e '{}\n{}' | passwd root".format(root_password,root_password))
        print(GREEN+"New password created successfully for root."+DEFAULT)
    else:
        print(RED+"Passwords not matched!"+DEFAULT)
        set_root_password()

#Getting new user credentials from user
def get_user_informations():
    os.system("clear")
    print("User Informations")

    global HOSTNAME
    HOSTNAME = input("\nHostname : ")

    global USERNAME
    USERNAME = input("\nUsername : ")

    global PASSWORD
    PASSWORD = input("\nPassword : ")
    REPEAT_PASSWORD = input("\nPassword Again : ")

    if PASSWORD == REPEAT_PASSWORD:
        print(GREEN+"[OK]"+DEFAULT)
    else:
        print(RED+"Wrong format!"+DEFAULT)
        get_user_informations()

#Creating new user
def create_user():
    os.system("clear")
    print("Creating user {}".format(USERNAME))
    os.system("useradd -m -g users -G wheel,storage,power,network,audio,video,optical -s /bin/bash {}".format(USERNAME))
    print(GREEN+"User {} created successfully.".format(USERNAME)+DEFAULT)

#Setting password for new user
def set_password():
    os.system("echo '{}\n{}' | passwd {} ".format(PASSWORD,PASSWORD,USERNAME))
    print(GREEN+"New password created successfully."+DEFAULT)

# Setting hostname
def set_hostname():
    os.system("echo {} > /etc/hostname".format(HOSTNAME))

def set_keyboard_map():
    os.system("clear")
    print("Keyboard Selection...\n")
    print("1 - List All Keyboard Layouts\n")
    print("2 - Search Keyboard Layout\n")
    print("3 - Set Keyboard Layout\n")

    response = input("Selection [1/2/3] : ")

    if response == '1':
        os.system("localectl list-keymaps")
        ret_back = input("Press any key for continue..")
        set_keyboard_map()
    elif response == '2':
        search_keyword = input("Enter the keyword you want to search : ")
        os.system("localectl list-keymaps | grep -i {}".format(search_keyword))
        ret_back = input("Press any key for continue..")
        set_keyboard_map()
    elif response == '3':
        keyboard_layout = input("Keyboard Layout : ")
        os.system("echo KEYMAP={} > /etc/vconsole.conf".format(keyboard_layout))
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        set_keyboard_map()

def set_locale():
    os.system("clear")
    print("Language And Localization...\n")
    print("1 - List All Languages\n")
    print("2 - Search Language\n")
    print("3 - Set Language\n")
    print("4 - Back (Keyboard Settings)")

    response = input("Selection [1/2/3] : ")

    if response == '1':
        os.system("more /etc/locale.gen")
        ret_back = input("Press any key for continue..")
        set_locale()
    elif response == '2':
        search_keyword = input("Enter the keyword you want to search : ")
        os.system("cat /etc/locale.gen | grep -i {}".format(search_keyword))
        ret_back = input("Press any key for continue..")
        set_locale()
    elif response == '3':
        system_language = input("Language : ")
        os.system("echo LANG={} > /etc/locale.conf".format(system_language))
    elif response == '4':
        set_keyboard_map()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        set_locale()

def main():
    set_root_password()
    get_user_informations()
    create_user()
    set_password()
    set_hostname()
    set_keyboard_map()

if __name__ == '__main__':
    main()
