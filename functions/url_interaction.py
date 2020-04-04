import os
import requests
import urllib.parse
from colorama import Fore

# - Color
red = Fore.LIGHTRED_EX
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.CYAN


def url_authen(url):
    os.system("dependency/vt url " + url + " --include=last_analysis_results.*.result")


def url_decode(url):
    print(green + "\n[*] " + white + "Basic Decode " + green + "[*]")
    basic_decode = urllib.parse.unquote(url)
    print(" ")
    print(blue, basic_decode)
    print(" ")
    print(green + "\n[*] " + white + "Parsed Decode " + green + "[*]")
    parse_decode = urllib.parse.parse_qs(url)
    print(" ")
    print(blue, parse_decode)


def http_status_code_and_header(url):
    request = requests.get(url)
    print(green + "\n[*] " + white + "Status Code: " + blue, request.status_code)
    print("")
    print(green + "\n[*] " + white + "Header " + green + "[*]")
    print("")
    for title, value in request.headers.items():
        print(yellow, title, ":", blue, value)


def html_metadata(url):
    request = requests.get(url)
    print(green + "\n[*] " + white + "Html Text " + green + "[*]")
    print(white, "")
    print(request.text)