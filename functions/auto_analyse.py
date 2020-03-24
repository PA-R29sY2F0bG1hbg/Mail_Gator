""""
	Auteur : Julien Michelet
	Date : mars 2020
	But du programme :
	Fonction automatique des fonctions suivantes :

	Version : 0.0
"""
import os
import sys
import datetime
from functions import email_identities


def auto_analyse_full(file):
    contenu = email_identities.all_meta_data_var(file)
    date = datetime.datetime.now()
    name_file = "file_analyse" + str(date) + ".txt"
    file_analyse = open("Repport.txt", "w")
    file_analyse.write("test lalalala \n")
    file_analyse.write(contenu)
    file_analyse.close()