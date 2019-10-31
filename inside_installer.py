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
        os.system('echo -e {}\n{} | passwd root'.format(root_password,root_password))
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
    print(GREEN+"User {} created successfully."+DEFAULT)

#Setting password for new user
def set_password():
    os.system("echo '{}\n{}' | passwd {} ".format(PASSWORD,PASSWORD,USERNAME))
    print(GREEN+"New password created successfully."+DEFAULT)

# Setting hostname
def set_hostname():
    os.system("echo {} > /etc/hostname".format(HOSTNAME))

def main():
    set_root_password()
    get_user_informations()
    create_user()
    set_password()
    set_hostname()

if __name__ == '__main__':
    main()
