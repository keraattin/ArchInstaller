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
    root_password = input("\nPlease enter the root password")
    os.system('echo -e {}\n{} | passwd root'.format(root_password,root_password))


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
