from colorama import Fore

# - Color
red = Fore.LIGHTRED_EX
white = Fore.LIGHTWHITE_EX
green = Fore.GREEN
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
blue = Fore.CYAN


# Main Menue
def main_menu():
    print(white + '\n                                   [/*\]' + green + ' Main Menu ' + white + '[/*\]')
    print("                                   --------------------- ")
    print(red + '\n[' + yellow + '1' + red + ']' + blue + ' Automatic Analyse')
    print(red + '[' + yellow + '2' + red + ']' + blue + ' Manual Analyse')
    print(white + '\n[' + green + '99' + white + ']' + yellow + ' Exit')


def manual_menu():
    print(white + '\n                            [/*\]' + green + ' Manual Analyse Menu ' + white + '[/*\]')
    print("                            ------------------------------- ")
    print(" ")
    print(" ")
    print(green + '[*]' + white + " Email Identities and Data " + green + '[*]', end='')
    print(green + '              [*]' + white + " Web Tracking Email Address " + green + '[*]')
    print("")
    print(red + '[' + yellow + '1' + red + ']' + blue + ' Full Email Metadata', end='')
    print(red + '                        [' + yellow + '4' + red + ']' + blue + ' Google Dorks')
    print(red + '[' + yellow + '2' + red + ']' + blue + ' Short list Metadata', end='')
    print(red + '                        [' + yellow + '5' + red + ']' + blue + ' Open Multiple Url From File')
    print(red + '[' + yellow + '3' + red + ']' + blue + ' Body Email Extract', end='')
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(green + '[*]' + white + " Email Adresse Check " + green + '[*]', end='')
    print(green + '                    [*]' + white + " IP Source Route" + green + '[*]')
    print(" ")
    print(red + '[' + yellow + '6' + red + ']' + blue + ' Hunter.IO', end='')
    print(red + '                                  [' + yellow + '8' + red + ']' + blue + ' traceroute')
    print(red + '[' + yellow + '7' + red + ']' + blue + ' Mail Hippo', end='')
    print(red + '                                 [' + yellow + '9' + red + ']' + blue + ' Geolocalisation')
    print(red + '                                               [' + yellow + '10' + red + ']' + blue + ' Last Servering IP')
    print(red + '                                               [' + yellow + '11' + red + ']' + blue + ' Url Authenticity')
    print(" ")
    print(" ")
    print(" ")
    print(green + '[*]' + white + " Malware Analyse " + green + '[*]', end='')
    print(green + '                        [*]' + white + " Volatility Memory " + green + '[*]')
    print(" ")
    print(red + '[' + yellow + '12' + red + ']' + blue + ' Get File Hash', end='')
    print(red + '                             [' + yellow + '14' + red + ']' + blue + ' Exiftool')
    print(red + '[' + yellow + '13' + red + ']' + blue + ' Analyse Attachment', end='')
    print(red + '                        [' + yellow + '15' + red + ']' + blue + ' Strings')
    print(red + '                                               [' + yellow + '16' + red + ']' + blue + ' hexdump')
    print(red + '                                               [' + yellow + '17' + red + ']' + blue + ' Pdf id')
    print(red + '                                               [' + yellow + '18' + red + ']' + blue + ' Pdf Parser')
    print(red + '                                               [' + yellow + '19' + red + ']' + blue + ' Office Doc Analyse & Macro')
    print(" ")
    print(white + '\n[' + green + '75' + white + ']' + yellow + ' Get Menue', end='')
    print(white + '\n[' + green + '50' + white + ']' + yellow + ' Return To Main Menu', end='')
    print(white + ' [' + green + '99' + white + ']' + yellow + ' Exit', end='')
    print(" ")
    print(" ")