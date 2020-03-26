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


def short_meta_data_var(file_mail):
    date = str(os.popen("grep ^Date: " + file_mail).readlines())
    subject = str(os.popen("grep ^Subject: " + file_mail).readlines())
    to_var = str(os.popen("grep ^To: " + file_mail).readlines())
    from_var = str(os.popen("grep ^From: " + file_mail).readlines())
    attachement = str(os.popen("grep attachement " + file_mail).readlines())
    message_id =str(os.popen("grep Message-Id: " + file_mail).readlines())
    received = os.popen("grep Received " + file_mail).readlines()
    smtp = os.popen("grep smtp " + file_mail).readlines()

    cont_tab = ("\n===============================",
                "\n[*] Short Meta Data Section [*]",
                "\n===============================",
                "\n\n[*] Global Informations [*]\n",
                "   ------------------------\n",
                date[2:(len(date)-4 )], "\n",
                subject[2:(len(subject) - 4)], "\n",
                to_var[2:(len(to_var) - 4)], "\n",
                from_var[2:(len(from_var) - 4)], "\n",
                attachement[2:(len(attachement) - 4)], "\n",
                str(message_id[2:(len(message_id) - 4)]), "\n\n",
                "[*] IP Information (Email Header) [*]", "\n",
                "   ------------------------", "\n",)
    cont_tab = cont_tab + tuple(received) + ("\n\n",) + \
               ("[*] SMTP Information [*]",) + ("\n",) +\
               ("   ------------------------",) + ("\n",) + \
               tuple(smtp) + ("\n",)

    return cont_tab


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
