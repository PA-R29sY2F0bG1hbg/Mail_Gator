import os
from colorama import Fore

# - Color
red = Fore.RED
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX


def exiftool(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("exiftool " + attachment)


def strings_tool(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("strings " + attachment)


def hexdump(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("hexdump -C " + attachment)


def pdfid(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    print("")
    os.system("python3 dependency/pdf_id/pdfid.py " + attachment)


def pdfparser(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("python3 dependency/pdf-parser.py " + attachment)

# test with csv or docx or more with macro
def oledump(attachment):
    print("\n[!] Imported File: ", attachment, "[!]\n")
    print("\n[*] Get Statistical Analysed of File \n")
    os.system("python3 dependency/oledump/oledump.py " + attachment)


def oledump_macro(A, attachment):
    print("\n[!] Imported File: ", attachment, "[!]\n")
    print("\n[*] Get Content of Macro \n")
    os.system("python3 dependency/oledump/elodump.py -s " + A + " -v " + attachment)
