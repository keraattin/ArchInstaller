#!usr/bin/env python3

import os
import sys
import math


#Colors
DEFAULT = "\33[37m"
GREEN = "\33[32m"
RED = "\33[31m"

#Welcome message function
def welcome():
    print(GREEN)    #For green output format
    print(" █████╗ ██████╗  ██████╗██╗  ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██║  ██║")
    print("███████║██████╔╝██║     ███████║")
    print("██╔══██║██╔══██╗██║     ██╔══██║")
    print("██║  ██║██║  ██║╚██████╗██║  ██║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print("                                ")
    print("██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗")
    print("██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗")
    print("██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝")
    print("██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗")
    print("██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║")
    print("╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝")
    print(DEFAULT)  #For default output format

    to_continue = input("Press any key to continue..")
    os.system("clear")

#Manual partitioning
def manual_partitioning():
    os.system("cfdisk") #For manual configuration
    os.system("clear")
    os.system("lsblk")  #Printing out patitions for checking configuration
    response = input("Are you sure about this configuration? [Y/n]")
    if response == 'Y' or response == 'y' or response == '':
        os.system("clear")
        return
    else:
        disk_partitioning()


def uefi_partitioning():
    efi_size = input("Insert EFI partition size [M/MiB - G/GiB] : ")
    if efi_size.find('M') != -1 or efi_size.find('MiB') != -1:
        found_point = efi_size.find('M')
        efi_part_size = efi_size[:found_point]
        efi_part_type = efi_size[found_point:]
        if efi_part_type == 'M' or efi_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    elif efi_size.find('G') != -1 or efi_size.find('GiB') != -1:
        found_point = efi_size.find('G')
        efi_part_size = efi_size[:found_point]
        efi_part_type = efi_size[found_point:]
        if efi_part_type == 'G' or efi_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            print(efi_part_type)
            uefi_partitioning()
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself

    boot_size = input("Insert /boot partition size [M/MiB - G/GiB] : ")
    if boot_size.find('M') != -1 or boot_size.find('MiB') != -1:
        found_point = boot_size.find('M')
        boot_part_size = boot_size[:found_point]
        boot_part_type = boot_size[found_point:]
        if boot_part_type == 'M' or boot_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    elif boot_size.find('G') != -1 or boot_size.find('GiB') != -1:
        found_point = boot_size.find('G')
        boot_part_size = boot_size[:found_point]
        boot_part_type = boot_size[found_point:]
        if boot_part_type == 'G' or boot_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself

    swap_size = input("Insert swap partition size [M/MiB - G/GiB] : ")
    if swap_size.find('M') != -1 or swap_size.find('MiB') != -1:
        found_point = swap_size.find('M')
        swap_part_size = swap_size[:found_point]
        swap_part_type = swap_size[found_point:]
        if swap_part_type == 'M' or swap_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    elif swap_size.find('G') != -1 or swap_size.find('GiB') != -1:
        found_point = swap_size.find('G')
        swap_part_size = swap_size[:found_point]
        swap_part_type = swap_size[found_point:]
        if swap_part_type == 'G' or swap_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself


    if efi_part_type == 'M' or efi_part_type == 'MiB':
        efi_start = 2048
        efi_end = efi_start + int((int(efi_part_size)*(math.pow(2,20)))/512)
    elif boot_part_type == 'G' or boot_part_type == 'GiB':
        efi_start = 2048
        efi_end = efi_start + int((int(efi_part_size)*(math.pow(2,30)))/512)

    if boot_part_type == 'M' or boot_part_type == 'MiB':
        boot_start = efi_end + 1
        boot_end = boot_start + int((int(boot_part_size)*(math.pow(2,20)))/512)
    elif boot_part_type == 'G' or boot_part_type == 'GiB':
        boot_start = efi_end + 1
        boot_end = boot_start + int((int(boot_part_size)*(math.pow(2,30)))/512)

    if swap_part_type == 'M' or swap_part_type == 'MiB':
        swap_start = boot_end + 1
        swap_end = swap_start + int((int(swap_part_size)*(math.pow(2,20)))/512)
    elif swap_part_type == 'G' or swap_part_type == 'GiB':
        swap_start = boot_end + 1
        swap_end = swap_start + int((int(swap_part_size)*(math.pow(2,30)))/512)


    print("Efi start : 2048")
    print("Efi end : " + str(efi_end))
    print("Boot start : " + str(boot_start))
    print("Boot end : " + str(boot_end))
    print("Swap start : " + str(swap_start))
    print("Swap end : " + str(swap_end))
    os.system("parted /dev/sda mklabel gpt --script") #Making label to gpt
    os.system("parted /dev/sda mkpart primary fat32 {} {} set 1 esp on --script".format(efi_start,efi_end))
    os.system("parted /dev/sda mkpart primary ext2 {} {} --script".format(boot_start,boot_end))
    os.system("parted /dev/sda mkpart primary linux-swap {} {} --script".format(swap_start,swap_end))
    #os.system("parted /dev/sda mkpart primary ext4 {} 100% --script".format(root_start))


def dos_partitioning():
    #os.system("parted /dev/sda mklabel msdos --script") #Making label to msdos
    print("auto")

def auto_partitioning():
    selection = input("1-UEFI (new) ,2-DOS (old) \nSelection [1/2] :")
    if selection == '1':
        uefi_partitioning()
    elif selection == '2':
        dos_partitioning()
    else:
        os.system("clear")
        print(RED+"Wrong Selection"+DEFAULT)
        auto_partitioning()


#Disk partitioning function
def disk_partitioning():
    selection = input("1-Auto Partitioning, 2-Manual Partitioning\nSelection [1/2] : ")
    if selection == '1':
        auto_partitioning()
    elif selection == '2':
        manual_partitioning()




def main():
    if os.geteuid() != 0:   #Check whether user have root privileges or not
        print(RED+"You are not root"+DEFAULT)
        sys.exit(1)
    welcome()
    disk_partitioning()

if __name__ == '__main__':
    main()
