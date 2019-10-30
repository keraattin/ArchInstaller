#!usr/bin/env python3

import os
import sys

#User Informations
HOSTNAME = ""
USERNAME = ""
PASSWORD = ""
ROOT_PASSWORD = ""

#Setting new password for root
def set_root_password():
    os.system("clear")
    root_password = input("\nPlease enter the root password")
    os.system('echo -e {}\n{} | passwd root'.format(root_password,root_password))
