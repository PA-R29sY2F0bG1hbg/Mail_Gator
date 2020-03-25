import os
import sys
import time
from functions import email_identities, exit, ip_tracking, \
    malware_vt_analyse, web_tracking_email, volatility_memory, \
    auto_analyse
from graphical import banner, menu
from colorama import Fore

#############
# Fixed Var #
#############
# - clear
os.system("clear")

# - user selection
user_selection = 0

# - Color
red = Fore.RED
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX

########
# Main #
########
try:
    # Import External File
    file = sys.argv[1]
    if len(sys.argv[2:]) == 0:
        pass
    else:
        attachment = sys.argv[2]

    # Main Loop
    banner.ban()
    menu.main_menu()
    while 1:
        user_input = int(input(white + "\nSelection: "))

        # Automatic Analyse
        if user_input == 1:
            try:
                auto_analyse.auto_analyse_full(file)
                print(green + "\n[*]" + white + " Report Generated " + green + "[*]" + white)
                print(red + "[*]" + yellow + " But Section In Development " + red + "[*]" + white)
                menu.main_menu()

            except KeyboardInterrupt:
                exit.exit_func()

        # Manual Analyse Menu
        if user_input == 2:
            os.system("clear")
            menu.manual_menu()
            while 1:
                user_input = int(input(white + '\nSelection: '))

                # Email ID Menu
                if user_input == 1:
                    email_identities.all_meta_data(file)
                elif user_input == 2:
                    email_identities.short_meta_data(file)
                elif user_input == 3:
                    email_identities.body_extract(file)

                # Web tracking Email Address
                elif user_input == 4:
                    inurl = input("\n[!] inurl: ")
                    intext = input("[!] intext: ")
                    url_number = int(input("[!] Enter Number of link wanted:"))
                    web_tracking_email.google_droks(inurl, intext, url_number)
                elif user_input == 5:
                    path_to_file = ("\n [!] Path To File: ")
                    web_tracking_email.open_multiple_url(path_to_file)

                # Email Addresse Check
                elif user_input == 6:
                    url = input("\n[!] Enter email addresse to check: ")
                    web_tracking_email.hunter_io(url)
                    time.sleep(1)
                    print(green, "\n[*] Hunter.io Loaded [*]")
                    time.sleep(1)
                elif user_input == 7:
                    web_tracking_email.email_hippo()
                    time.sleep(1)
                    print(green, "\n[*] Hunter.io Loaded [*]")
                    time.sleep(1)

                # IP Source Route
                elif user_input == 8:
                    targer_ip = input("\n[!] Enter Target IP: ")
                    ip_tracking.trace_route(targer_ip)
                elif user_input == 9:
                    targer_ip = input("\n[!] Enter Target IP: ")
                    time.sleep(1)
                    ip_tracking.map_geo(targer_ip)
                    print(green, "\n[*] IPLeak Loaded [*]")
                    time.sleep(1)
                elif user_input == 10:
                    target_url = input("[!] Enter url: ")
                    ip_tracking.last_servering_ip(target_url)
                elif user_input == 11:
                    target_url = input("[!] Enter url: ")
                    ip_tracking.url_authen(target_url)

                # Malware Analyse
                elif user_input == 12:
                    malware_vt_analyse.get_attachment_hash(attachment)
                elif user_input == 13:
                    hash_file = input("[!] Enter File Hash: ")
                    malware_vt_analyse.analyse_attachment(hash_file)

                # Volatility Memory
                elif user_input == 14:
                    volatility_memory.exiftool(attachment)
                elif user_input == 15:
                    volatility_memory.strings_tool(attachment)
                elif user_input == 16:
                    volatility_memory.hexdump(attachment)
                elif user_input == 17:
                    volatility_memory.pdfid(attachment)
                elif user_input == 18:
                    volatility_memory.pdfparser(attachment)
                elif user_input == 19:
                    volatility_memory.oledump(attachment)
                    A = input("Select Macro To Analyse: ")  # In development
                    volatility_memory.oledump_macro(A, attachment)

                # GM / QUI / BACK
                elif user_input == 75:
                    menu.manual_menu()
                elif user_input == 50:
                    menu.main_menu()
                    break
                elif user_input == 99:
                    exit.exit_func()

        # Exit Mail Gator
        elif user_input == 99:
            exit.exit_func()


except IndexError:
    print(red, "\n [!] Usage: ./main.py [path to email] [(optional) path to attachment] [!] \n")

except KeyboardInterrupt:
    exit.exit_func()
