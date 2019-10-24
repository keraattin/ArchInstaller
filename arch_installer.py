#!usr/bin/env python3

import os
import sys
import math


#Colors
DEFAULT = "\33[37m"
GREEN = "\33[32m"
RED = "\33[31m"
CYAN = "\33[36m"
MAGENTA = "\33[35m"

#Consts
SECTOR_SIZE = 512   #1 sector 512Byte
MEGABYTE = math.pow(2,20)
GIGABYTE = math.pow(2,30)

#User Informations
USERNAME = ""
PASSWORD = ""

#Welcome message function
def welcome():
    os.system("clear")
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
    os.system("clear")
    efi_size = input("Insert EFI partition size [M/MiB - G/GiB] : ")
    if efi_size.find('M') != -1 or efi_size.find('MiB') != -1:
        found_point = efi_size.find('M')
        efi_part_size = int(efi_size[:found_point])
        efi_part_type = efi_size[found_point:]
        efi_sector_start = 2048 #First sector
        efi_sector_end = efi_sector_start + int((int(efi_part_size)*MEGABYTE)/SECTOR_SIZE)
        efi_sector = int((int(efi_part_size)*MEGABYTE)/SECTOR_SIZE)
        efi_part_start = 1
        efi_part_end = efi_part_size
        if efi_part_type == 'M' or efi_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning() #If wrong format entered, call again itself
    elif efi_size.find('G') != -1 or efi_size.find('GiB') != -1:
        found_point = efi_size.find('G')
        efi_part_size = int(efi_size[:found_point])
        efi_part_type = efi_size[found_point:]
        efi_sector_start = 2048 #First sector
        efi_sector_end = efi_sector_start + int((int(efi_part_size)*GIGABYTE)/SECTOR_SIZE)
        efi_sector = int((int(efi_part_size)*GIGABYTE)/SECTOR_SIZE)
        efi_part_start = 1
        efi_part_end = int(efi_part_size * 1024)
        if efi_part_type == 'G' or efi_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning() #If wrong format entered, call again itself
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself

    boot_size = input("Insert /boot partition size [M/MiB - G/GiB] : ")
    if boot_size.find('M') != -1 or boot_size.find('MiB') != -1:
        found_point = boot_size.find('M')
        boot_part_size = int(boot_size[:found_point])
        boot_part_type = boot_size[found_point:]
        boot_sector_start = efi_sector_end + 1
        boot_sector_end = boot_sector_start + int((int(boot_part_size)*MEGABYTE)/SECTOR_SIZE)
        boot_sector = int((int(boot_part_size)*MEGABYTE)/SECTOR_SIZE)
        boot_part_start = efi_part_end
        boot_part_end = boot_part_start + boot_part_size
        if boot_part_type == 'M' or boot_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning() #If wrong format entered, call again itself
    elif boot_size.find('G') != -1 or boot_size.find('GiB') != -1:
        found_point = boot_size.find('G')
        boot_part_size = int(boot_size[:found_point])
        boot_part_type = boot_size[found_point:]
        boot_sector_start = efi_sector_end + 1
        boot_sector_end = boot_sector_start + int((int(boot_part_size)*GIGABYTE)/SECTOR_SIZE)
        boot_sector = int((int(boot_part_size)*GIGABYTE)/SECTOR_SIZE)
        boot_part_start = efi_part_end
        boot_part_end = boot_part_start + int(boot_part_size*1024)
        if boot_part_type == 'G' or boot_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning() #If wrong format entered, call again itself
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself

    swap_size = input("Insert swap partition size [M/MiB - G/GiB] : ")
    if swap_size.find('M') != -1 or swap_size.find('MiB') != -1:
        found_point = swap_size.find('M')
        swap_part_size = int(swap_size[:found_point])
        swap_part_type = swap_size[found_point:]
        swap_sector_start = boot_sector_end + 1
        swap_sector_end = swap_sector_start + int((int(swap_part_size)*MEGABYTE)/SECTOR_SIZE)
        swap_sector = int((int(swap_part_size)*MEGABYTE)/SECTOR_SIZE)
        swap_part_start = boot_part_end
        swap_part_end = swap_part_start + swap_part_size
        if swap_part_type == 'M' or swap_part_type == 'MiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning() #If wrong format entered, call again itself
    elif swap_size.find('G') != -1 or swap_size.find('GiB') != -1:
        found_point = swap_size.find('G')
        swap_part_size = int(swap_size[:found_point])
        swap_part_type = swap_size[found_point:]
        swap_sector_start = boot_sector_end + 1
        swap_sector_end = swap_sector_start + int((int(swap_part_size)*GIGABYTE)/SECTOR_SIZE)
        swap_sector = int((int(swap_part_size)*GIGABYTE)/SECTOR_SIZE)
        swap_part_start = boot_part_end
        swap_part_end = swap_part_start + int(swap_part_size*1024)
        if swap_part_type == 'G' or swap_part_type == 'GiB':
            print(GREEN+"[OK]"+DEFAULT)
        else:
            print(RED+"Wrong format!"+DEFAULT)
            uefi_partitioning()
    else:
        print(RED+"Wrong format entered.\nEnter size like 100M or 100MiB"+DEFAULT)
        uefi_partitioning() #If wrong format entered, call again itself

    print(CYAN+"{:<10s}{:<10s}{:<10s}{:<14s}{:<14s}{:<14s}".format("Type","Start","Stop","Start Sector","End Sector","Sector"+DEFAULT))
    print("{:<10s}{:<10s}{:<10s}{:<14s}{:<14s}{:<14s}".format("Efi",str(efi_part_start),str(efi_part_end),str(efi_sector_start),str(efi_sector_end),str(efi_sector)))
    print("{:<10s}{:<10s}{:<10s}{:<14s}{:<14s}{:<14s}".format("Boot",str(boot_part_start),str(boot_part_end),str(boot_sector_start),str(boot_sector_end),str(boot_sector)))
    print("{:<10s}{:<10s}{:<10s}{:<14s}{:<14s}{:<14s}".format("Swap",str(swap_part_start),str(swap_part_end),str(swap_sector_start),str(swap_sector_end),str(swap_sector)))

    response = input("Are you sure about this configuration? [Y/n]")
    if response == 'Y' or response == 'y' or response == '':
        os.system("parted /dev/sda mklabel gpt --script") #Making label to gpt
        os.system("parted /dev/sda mkpart primary fat32 {}M {}M set 1 esp on --script".format(efi_part_start,efi_part_end)) #Creating efi partition
        os.system("parted /dev/sda mkpart primary ext2 {}M {}M --script".format(boot_part_start,boot_part_end)) #Creating boot partition
        os.system("parted /dev/sda mkpart primary linux-swap {}M {}M --script".format(swap_part_start,swap_part_end)) #Creating swap partition
        os.system("parted /dev/sda mkpart primary ext4 {}M 100% --script".format(swap_part_end)) #Creating root partition

        #Formatting partitions
        os.system("yes | mkfs.vfat -F32 /dev/sda1")
        os.system("yes | mkfs.ext2 /dev/sda2")
        os.system("yes | mkswap /dev/sda3")
        os.system("yes | mkfs.ext4 /dev/sda4")
    else:
        disk_partitioning()


def dos_partitioning():
    #os.system("parted /dev/sda mklabel msdos --script") #Making label to msdos
    print("auto")

def auto_partitioning():
    os.system("clear")
    print("Auto Partitioning...\n")
    selection = input("1-UEFI (new systems)\n\n2-DOS (old systems)\n\n3-Back\n\nSelection [1/2/3] : ")
    if selection == '1':
        os.system("clear")
        print("Auto Partitioning -> UEFI")
        prompt = input("1-Erase Disk And Install Arch Linux\n\n2-Guided UEFI Installation\n\n3-Back\n\nSelection[1/2/3] : ")
        if prompt == '1':
            print()
        elif prompt == '2':
            uefi_partitioning()
        elif prompt == '3':
            auto_partitioning()
        else:
            os.system("clear")
            print(RED+"Wrong Selection"+DEFAULT)
            auto_partitioning()
    elif selection == '2':
        os.system("clear")
        print("Auto Partitioning -> UEFI")
        prompt = input("1-Erase Disk And Install Arch Linux\n\n2-Guided DOS Installation\n\n3-Back\n\nSelection[1/2/3] : ")
        if prompt == '1':
            print()
        elif prompt == '2':
            dos_partitioning()
        elif prompt == '3':
            auto_partitioning()
        else:
            os.system("clear")
            print(RED+"Wrong Selection"+DEFAULT)
            auto_partitioning()
    elif selection == '3':
        disk_partitioning()
    else:
        os.system("clear")
        print(RED+"Wrong Selection"+DEFAULT)
        auto_partitioning()


#Mounting disk volumes to /mnt
def mount_volume():
    os.system("mount /dev/sda4 /mnt")
    os.system("mkdir /mnt/boot")
    os.system("mount /dev/sda2 /mnt/boot")
    os.system("mkdir /mnt/boot/efi")
    os.system("mount /dev/sda1 /mnt/boot/efi")
    os.system("swapon /dev/sda3")

#Getting new user credentials from user
def get_user_informations():
    os.system("clear")
    print("User Informations")
    USERNAME = input("\nUsername : ")
    PASSWORD = input("\nPassword : ")

#Installing base packages to /mnt
def install_necessarily_packages():
    os.system("pacstrap /mnt base base-devel grub os-prober")

#Generating fstab file for mounted volumes
def generate_fstab():
    os.system("genfstab -U -p >> /mnt >> /mnt/etc/fstab")

#Disk partitioning function
def disk_partitioning():
    os.system("clear")
    selection = input("1-Auto Partitioning\n\n2-Manual Partitioning\n\n3-Exit\n\nSelection [1/2/3] : ")
    if selection == '1':
        auto_partitioning()
    elif selection == '2':
        manual_partitioning()
    elif selection == '3':
        sys.exit(1)
    else:
        print(RED+"Wrong Selection"+DEFAULT)
        disk_partitioning()


def main():
    if os.geteuid() != 0:   #Check whether user have root privileges or not
        print(RED+"You are not root"+DEFAULT)
        sys.exit(1)
    welcome()
    disk_partitioning()
    mount_volume()
    install_necessarily_packages()
    generate_fstab()

if __name__ == '__main__':
    main()
