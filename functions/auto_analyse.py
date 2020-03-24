""""
	Auteur : Julien Michelet
	Date : mars 2020
	But du programme :
	Fonction automatique des fonctions suivantes :

	Version : 0.0
"""
import os
import sys
from functions import email_identities


def auto_analyse_full(file):
    contenu = email_identities.all_meta_data_var(file)
    name_file = "file_analyse" + + ".txt"
    file_analyse = open("file_analyse.txt","w")
    file_analyse.write("test lalalala \n")
    file_analyse.write(contenu)
    file_analyse.close()

file = "/root/Téléchargements/Mail_Gator-master/cadeaux_destines_aux_clients_de_LiDL..eml"
auto_analyse_full(file)