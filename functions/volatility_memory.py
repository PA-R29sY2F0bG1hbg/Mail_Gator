import os


def exiftool(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("exiftool " + attachment)


def strings_tool(attachment):
    print("\n[*] Imported File: ", attachment, "[*]\n")
    os.system("strings " + attachment)
