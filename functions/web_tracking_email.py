from googlesearch import search
from colorama import Fore
import subprocess
import webbrowser

# - Color
red = Fore.RED
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.LIGHTBLUE_EX

# See Update
# Maybe Multiple Dorks
# Or Dorks Slection


def google_droks(dorks, dorks2, link_number):
    inurl = "inurl:"
    intext = "intext:"
    query = inurl + dorks + " " + intext + dorks2
    try:
        for j in search(query, tld="co.in", num=10, stop=link_number):
            print(blue+j)

    except:
        print(red, "\n [!] Possibly Not Working Cause Of To Many Request With This IP [!]")


def hunter_io(url):
    pre_fix = "https://hunter.io/email-verifier/"
    subprocess.Popen(["firefox", pre_fix+url])


def email_hippo():
    subprocess.Popen(["firefox", "https://tools.verifyemailaddress.io/"])


def open_multiple_url(path):
    lineList = list()
    print("")
    urlList = [line.rstrip('\n') for line in open(path)]
    for url in urlList:
        print("\n[*] Url Opened [*]")
        print(url)
        webbrowser.open(url)