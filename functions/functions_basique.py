import os


def search_word(string, mot_debut, mot_fin):
    debut = string.find(mot_debut)
    fin = string.rfind(mot_fin)

    return string[debut:fin-1]


def search_word_add_string(string, mot, string_add):
    fin = string.find(mot) + len(mot) + 1
    string = string[:fin] + string_add[0:len(string_add)] + string[fin+len(string_add):]

    return string


def read_file(file):
    fichier = open(file, "r")
    contenu = fichier.read()
    fichier.close()
    return contenu


"""
report_header = "/root/cadeaux_destines_aux_clients_de_LiDL..eml"
file_header = open(report_header, "r")
contenu_header = file_header.read()
file_header.close()

print(search_word(contenu_header, "Date: ", "Content-Type: "))
"""
