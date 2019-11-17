#!usr/bin/env python3

import os
import sys
import subprocess

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

#System Informations
DISPLAY_MANAGER = ""
DESKTOP_MANAGER = ""

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

#Adding new user to sudoers file
def add_user_to_sudoers():
    os.system("sed -i '82 s/^#//g' /etc/sudoers") #Uncomment wheel
    os.system("sed -i '85 s/^#//g' /etc/sudoers") #Uncomment wheel:nopasswd
    os.system("sed -i '88 s/^#//g' /etc/sudoers") #Uncomment sudo

#Setting hostname
def set_hostname():
    os.system("echo {} > /etc/hostname".format(HOSTNAME))

#Setting keyboard map
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
        try:
            is_valid = subprocess.check_output("localectl list-keymaps | grep -w -o -c {}".format(keyboard_layout), shell=True)
            if is_valid.rstrip().decode() == '1':
                os.system("echo KEYMAP={} > /etc/vconsole.conf".format(keyboard_layout))
            else:
                print(RED+"Wrong Keyboard Map!"+DEFAULT)
                set_keyboard_map()
        except:
            print(RED+"Wrong Keyboard Map!"+DEFAULT)
            set_keyboard_map()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        set_keyboard_map()

#Setting Localization
def set_locale():
    os.system("clear")
    print("Language And Localization...\n")
    print("1 - List All Languages\n")
    print("2 - Search Language\n")
    print("3 - Set Language\n")
    print("4 - Back (Keyboard Settings)")

    response = input("Selection [1/2/3/4] : ")

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
        system_language = input("Language [tr_TR,en_US] : ")
        try:
            is_valid = subprocess.check_output("cat /etc/locale.gen | grep -w -o -c {}".format(system_language), shell=True)
            if int(is_valid.rstrip().decode()) >= 1:
                os.system("echo LANG={}.UTF-8 > /etc/locale.conf".format(system_language))
                os.system("echo LANGUAGE={} >> /etc/locale.conf".format(system_language))
                os.system("echo LC_ALL=C >> /etc/locale.conf".format(system_language))
                os.system("locale-gen")
            else:
                print(RED+"Wrong Localization!"+DEFAULT)
                set_locale()
        except:
            print(RED+"Wrong Localization!"+DEFAULT)
            set_locale()

    elif response == '4':
        set_keyboard_map()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        set_locale()

#Setting Timezone
def set_timezone():
    os.system("clear")
    print("Timezone Selection...\n")
    print("1 - List All Timezones\n")
    print("2 - Search Timezone\n")
    print("3 - Set Timezone\n")
    print("4 - Back (Language And Localization)")

    response = input("Selection [1/2/3/4] : ")

    if response == '1':
        os.system("timedatectl list-timezones")
        ret_back = input("Press any key for continue..")
        set_timezone()
    elif response == '2':
        search_timezone = input("Enter the timezone you want to search : ")
        os.system("timedatectl list-timezones | grep -i {}".format(search_timezone))
        ret_back = input("Press any key for continue..")
        set_timezone()
    elif response == '3':
        system_timezone = input("Timezone [Europe/Istanbul] : ")
        try:
            is_valid = subprocess.check_output("timedatectl list-timezones | grep -w -o -c {}".format(system_timezone), shell=True)
            if is_valid.rstrip().decode() == '1':
                os.system("echo {} > /etc/timezone".format(system_timezone))
                os.system("ln -s /usr/share/zoneinfo/{} /etc/localtime".format(system_timezone))
                os.system("hwclock --systohc --utc")
        except:
            print(RED+"Wrong Timezone!"+DEFAULT)
            set_timezone()
    elif response == '4':
        set_locale()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        set_timezone()

#Installing and enabling Network Manager
def install_network_manager():
    os.system("yes | pacman -S networkmanager dialog")
    os.system("systemctl enable NetworkManager")

#Installing Xorg and Utils
def install_xorg():
    os.system("echo -e '\n\n' | pacman -S xorg xorg-xinit xorg-xclock xorg-twm xterm mesa alsa alsa-lib alsa-utils dbus")

#Installing LightDM Display Manager
def install_ligthdm():
    os.system("echo -e '\n' | pacman -S lightdm lightdm-gtk-greeter")
    os.system("systemctl enable lightdm")

#Installing Sddm Display Manager
def install_sddm():
    os.system("echo -e '\n' | pacman -S sddm")
    os.system("systemctl enable sddm")

#Installing Gdm Gnome Display Manager
def install_gdm():
    os.system("echo -e '\n' | pacman -S gdm")
    os.system("systemctl enable gdm")

#Installing Display Manager
def install_display_manager(display_manager):
    if display_manager == "lightdm":
        install_ligthdm()
    elif display_manager == "sddm":
        install_sddm()
    elif display_manager == "gdm":
        install_gdm()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        select_display_manager()

#Display Manager Selection
def select_display_manager():
    os.system("clear")
    print("Display Manager...\n")
    print("1 - Lightdm\n")
    print("2 - Sddm\n")
    print("3 - Gdm\n")

    response = input("Selection [1/2/3] : ")

    if response == '1':
        print("Lightdm\n")
        control = input("Installing Lightdm, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DISPLAY_MANAGER
            DISPLAY_MANAGER = "lightdm"
    elif response == '2':
        print("Sddm\n")
        control = input("Installing Sddm, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DISPLAY_MANAGER
            DISPLAY_MANAGER = "sddm"
    elif response == '3':
        print("Gdm\n")
        control = input("Installing Gdm, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DISPLAY_MANAGER
            DISPLAY_MANAGER = "gdm"
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        select_display_manager()


#Installing Xfce Desktop Manager
def install_xfce():
    os.system("echo -e '\n\n' | pacman -S xfce4 xfce4-goodies")

#Installing KDE Desktop Manager
def install_kde():
    os.system("echo -e '\n\n\n\n' | pacman -S plasma kdebase")

#Installing Gnome Desktop Manager
def install_gnome():
    os.system("echo -e '\n\n' | pacman -S gnome gnome-extra")

#Installing Desktop Manager
def install_desktop_manager(desktop_manager):
    if desktop_manager == "xfce":
        install_xfce()
    elif desktop_manager == "kde":
        install_kde()
    elif desktop_manager == "gnome":
        install_gnome()
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        select_desktop_manager()

#Desktop Manager Selection
def select_desktop_manager():
    os.system("clear")
    print("Desktop Manager...\n")
    print("1 - Xfce\n")
    print("2 - KDE\n")
    print("3 - Gnome\n")

    response = input("Selection [1/2/3] : ")

    if response == '1':
        control = input("Installing Xfce, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DESKTOP_MANAGER
            DISPLAY_MANAGER = "xfce"
    elif response == '2':
        control = input("Installing KDE, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DESKTOP_MANAGER
            DISPLAY_MANAGER = "kde"
    elif response == '3':
        control = input("Installing Gnome, are you sure? [Y/n]")
        if control == 'Y' or control == 'y' or control == '':
            global DESKTOP_MANAGER
            DISPLAY_MANAGER = "gnome"
    else:
        print(RED+"Wrong Selection!"+DEFAULT)
        select_desktop_manager()

#Adding additional repositories
def add_repositories():
    os.system("sed -i '92,93 s/^#//g' /etc/pacman.conf") #Enabling Multilib

    #Archlinuxfr
    os.system("echo -e '\n' >> /etc/pacman.conf")
    os.system("echo '[archlinuxfr]' >> /etc/pacman.conf")
    os.system("echo 'SigLevel = Never' >> /etc/pacman.conf")
    os.system("echo 'Server = http://repo.archlinux.fr/$arch' >> /etc/pacman.conf")

    #Archlinuxcn
    os.system("echo -e '\n' >> /etc/pacman.conf")
    os.system("echo '[archlinuxcn]' >> /etc/pacman.conf")
    os.system("echo 'SigLevel = Optional TrustedOnly' >> /etc/pacman.conf")
    os.system("echo 'Server = http://repo.archlinuxcn.org/$arch' >> /etc/pacman.conf")

    #Herecura
    os.system("echo -e '\n' >> /etc/pacman.conf")
    os.system("echo '[herecura]' >> /etc/pacman.conf")
    os.system("echo 'Server = http://repo.herecura.be/herecura/x86_64' >> /etc/pacman.conf")

#Updating keyrings
def update_keyrings():
    os.system("rm -r /etc/pacman.d/gnupg")
    os.system("pacman-key --init")
    os.system("pacman-key --populate archlinux")
    os.system("pacman -Syyu")

#Installing yaourt
def install_yaourt():
    os.system("echo -e '\n' | pacman -Sy yaourt")

#Installing utilities
def install_utilities():
    os.system("echo -e '\n' | pacman -S firefox zlib p7zip unzip zip unrar opendesktop-fonts")

#Mkinit
def mkinit():
    os.system("mkinitcpio -p linux")

#Installing grub
def install_grub():
    os.system("grub-install /dev/sda")
    os.system("grub-mkconfig -o /boot/grub/grub.cfg")
    os.system("grub-install --recheck /dev/sda")

def main():
    set_root_password()
    get_user_informations()
    create_user()
    set_password()
    add_user_to_sudoers()
    set_hostname()
    set_keyboard_map()
    set_locale()
    set_timezone()
    select_display_manager(DISPLAY_MANAGER)
    select_desktop_manager(DESKTOP_MANAGER)
    install_network_manager()
    install_xorg()
    install_display_manager()
    install_desktop_manager()
    install_utilities()
    add_repositories()
    update_keyrings()
    install_yaourt()
    mkinit()
    install_grub()

if __name__ == '__main__':
    main()
