import os
import sys
import time
from functions import email_identities, exit, ip_tracking, \
    malware_vt_analyse, web_tracking_email, volatility_memory
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
        user_input = int(input("\n Selection: "))

        # Automatic Analyse
        if user_input == 1:
            try:
                while 1:
                    print("Automatic Analyse")
            except KeyboardInterrupt:
                exit.exit_func()

        # Manual Analyse Menu
        if user_input == 2:
            while 1:
                menu.manual_menu()
                user_input = int(input('\n Selection: '))

                # Email ID Menu
                if user_input == 1:
                    while 1:
                        menu.email_id_menu()
                        user_input = int(input('\n Selection: '))

                        # All Email  Meta Data
                        if user_input == 1:
                            email_identities.all_meta_data(file)

                        # Shot Meta Data
                        elif user_input == 2:
                            email_identities.short_meta_data(file)

                        # Extract Body Email
                        elif user_input == 3:
                            email_identities.body_extract(file)

                        # Return To main Menu
                        elif user_input == 50:
                            break

                        # Exit Mail Gator
                        elif user_input == 99:
                            exit.exit_func()

                # Web Tracking Menu + Under Menu Ref Website
                elif user_input == 2:
                    while 1:
                        menu.web_tracking()
                        user_input = int(input('\n Selection: '))

                        # Google Dorks
                        if user_input == 1:
                            email_domain = input("\n[!] inurl: ")
                            prefix_email = input("[!] intext: ")
                            url_number = int(input("[!] Enter Number of link wanted:"))
                            web_tracking_email.google_droks(email_domain, prefix_email, url_number)

                        # Open Multiple Url From File
                        elif user_input == 2:
                            file_path = email_target = input("[!] Enter Complet Path To File: ")
                            web_tracking_email.open_multiple_url(file_path)

                        # Reffered Website
                        elif user_input == 3:
                            while 1:
                                menu.refered_websit()
                                user_input = int(input('\n Selection: '))

                                # Hunter.IO
                                if user_input == 1:
                                    url = input("\n[!] Enter email addresse to check: ")
                                    web_tracking_email.hunter_io(url)
                                    time.sleep(1)
                                    print(green, "\n[*] Hunter.io Loaded [*]")
                                    time.sleep(1)

                                # Email Hippo
                                elif user_input == 2:
                                    web_tracking_email.email_hippo()
                                    time.sleep(1)
                                    print(green, "\n[*] Hunter.io Loaded [*]")
                                    time.sleep(1)

                                # Back To Second Menu
                                elif user_input == 50:
                                    menu.refered_websit()
                                    break
                                elif user_input == 99:
                                    exit.exit_func()

                        # Back To Main Menu
                        elif user_input == 50:
                            menu.main_menu()
                            break

                        # Exit EmailGator
                        elif user_input == 99:
                            exit.exit_func()

                # ip source route menu
                elif user_input == 3:
                    while 1:
                        menu.ip_source_route()
                        user_input = int(input('\n Selection: '))

                        # traceroute & whois
                        if user_input == 1:
                            targer_ip = input("\n[!] Enter Target IP: ")
                            ip_tracking.trace_route(targer_ip)

                        # Website IPleak (GeoLoca)
                        elif user_input == 2:
                            targer_ip = input("\n[!] Enter Target IP: ")
                            time.sleep(1)
                            ip_tracking.map_geo(targer_ip)
                            print(green, "\n[*] IPLeak Loaded [*]")
                            time.sleep(1)

                        # vt - analyse url
                        elif user_input == 3:
                            target_url = input("[!] Enter url: ")
                            ip_tracking.last_servering_ip(target_url)

                        # vt - url authenticity
                        elif user_input == 4:
                            target_url = input("[!] Enter url: ")
                            ip_tracking.url_authen(target_url)

                        # back to main menu
                        elif user_input == 50:
                            menu.main_menu()
                            break

                        # Exit Mail_Gator
                        elif user_input == 99:
                            exit.exit_func()

                # Malware Analyse
                elif user_input == 4:
                    while 1:
                        menu.vt_analyse()
                        user_input = int(input('\n Selection: '))

                        # get Hash attachment
                        if user_input == 1:
                            malware_vt_analyse.get_attachment_hash(attachment)

                        # analyse Attachment
                        elif user_input == 2:
                            input_hash = input("[!] Enter File Hash: ")
                            malware_vt_analyse.analyse_attachment(input_hash)

                        # Back To main Menu
                        elif user_input == 50:
                            menu.main_menu()
                            break

                        # Exit Mail_Gator
                        elif user_input == 99:
                            exit.exit_func()

                # Volatility Memory
                elif user_input == 5:
                    while 1:
                        menu.volatility_m()
                        user_input = int(input("\nSelection: "))

                        # ExifTool
                        if user_input == 1:
                            volatility_memory.exiftool(attachment)

                        # Strings Tool
                        elif user_input == 2:
                            volatility_memory.strings_tool(attachment)

                        # hexdump Tool
                        elif user_input == 3:
                            volatility_memory.hexdump(attachment)

                        # PDF ID Tool
                        elif user_input == 4:
                            volatility_memory.pdfid(attachment)

                        # PDF PARSER Tool
                        elif user_input == 5:
                            volatility_memory.pdfparser(attachment)

                        # OLEDUMP Tool
                        elif user_input == 6:
                            volatility_memory.oledump(attachment)
                            A = input("Select Macro To Analyse: ")  # In development
                            volatility_memory.oledump_macro(A, attachment)

                        # Exit Mail Gator
                        elif user_input == 99:
                            exit.exit_func()

                # Back To Main Menu
                elif user_input == 50:
                    break

                # Exit Mail Gator
                elif user_input == 99:
                    exit.exit_func()

        # Exit Mail Gator
        elif user_input == 99:
            exit.exit_func()


except IndexError:
    print(red, "\n [!] Usage: ./main.py [path to email] [(optional) path to attachment] [!] \n")

except KeyboardInterrupt:
    exit.exit_func()
