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


"""Ecriture dans un fichier en passant le nom du fichier, son contenu et type d'écriture ( a, ,w ..)"""
def write_file(name_file, contenu, choix_write):
    file_analyse = open(name_file, choix_write)
    file_analyse.write(contenu)
    file_analyse.close()


def write_file_tableau(name_file, contenu, choix_write):
    file_analyse = open(name_file, choix_write)
    for i in range(len(contenu)):
        file_analyse.write(contenu[i])
    file_analyse.close()


def read_file_write_report(report_header, name_file, choix_write):
    file_header = open(report_header, "r")
    contenu_header = file_header.read()
    file_header.close()
    write_file(name_file, contenu_header, choix_write)
"""
report_header = "/root/cadeaux_destines_aux_clients_de_LiDL..eml"
file_header = open(report_header, "r")
contenu_header = file_header.read()
file_header.close()

print(search_word(contenu_header, "Date: ", "Content-Type: "))
"""
