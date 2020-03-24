import os
import mailparser
from colorama import Fore

# - Color
red = Fore.RED
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX


def all_meta_data(file):
    os.system("clear")
    os.system('cat ' + file)


def all_meta_data_var(file):
    file = open(file, "r")
    contenu = file.read()
    file.close()
    return contenu


def short_meta_data(file):
            os.system("clear")
            print("\n")
            print("\n [*] Global Informations [*]")
            print("   ------------------------")
            e_date = os.system("grep ^Date " + file)
            e_sub = os.system("grep ^Subject " + file)
            e_to = os.system("grep ^To: " + file)
            e_from = os.system("grep ^From: " + file)
            e_attach = os.system("grep attachment " + file)
            e_mess_id = os.system("grep Message-Id: " + file)
            print("\n [*] IP Information (Email Header) [*]")
            print("  --------------------")
            e_rcv_ip = os.system("grep Received " + file)
            print("\n [*] SMTP Inforamtion [*] ")
            print("  ----------------------")
            e_smtp = os.system("grep smtp " + file)


def short_meta_data_var(file, report):
    space = os.system('echo " "' + ">>" + report)
    head = os.system('echo "==============================="' + ">>" + report)
    head = os.system('echo "[*] Short Meta Data Section [*]"' + ">>" + report)
    head = os.system('echo "==============================="' + ">>" + report)
    space = os.system('echo " "' + ">>" + report)
    head1 = os.system('echo "[*] Global Informations [*]"' + ">>" + report)
    sep = os.system('echo "   ------------------------"' + ">>" + report)
    e_date = os.system("grep ^Date " + file + ">>" + report)
    e_sub = os.system("grep ^Subject " + file + ">>" + report)
    e_to = os.system("grep ^To: " + file + ">>" + report)
    e_from = os.system("grep ^From: " + file + ">>" + report)
    e_attach = os.system("grep attachment " + file + ">>" + report)
    e_mess_id = os.system("grep Message-Id: " + file + ">>" + report)
    space = os.system('echo " "' + ">>" + report)
    head2 = os.system('echo "[*] IP Information (Email Header) [*]"' + ">>" + report)
    sep = os.system('echo "   ------------------------"' + ">>" + report)
    e_rcv_ip = os.system("grep Received " + file + ">>" + report)
    space = os.system('echo " "' + ">>" + report)
    head3 = os.system('echo "[*] SMTP Inforamtion [*]"' + ">>" + report)
    sep = os.system('echo "   ------------------------"' + ">>" + report)
    e_smtp = os.system("grep smtp " + file + ">>" + report)


def body_extract(file):
    mail = mailparser.parse_from_file(file)
    os.system("clear")
    print("\n [*] BODY [*] ")
    print("  ----------")
    print("\n")
    print(mail.body)
    print("\n")


def body_extract_var(file):
    mail = mailparser.parse_from_file(file)
    return mail.body
