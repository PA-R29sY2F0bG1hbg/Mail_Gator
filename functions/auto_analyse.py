""""
	Auteur : Julien Michelet
	Date : mars 2020
	But du programme :
	Fonction automatique des fonctions suivantes :

	Version : 0.0
"""
import os
import sys
import time
from graphical import report_header
from datetime import datetime
from functions import email_identities

today_date = datetime.now()
report_date = "\nDATE: ", str(today_date.month) + str(today_date.day) + str(today_date.year) \
              + str(today_date.hour) + str(today_date.minute)


def write_file(name_file, contenu, choix_write):
    file_analyse = open(name_file, choix_write)
    file_analyse.write(contenu)
    file_analyse.close()

def write_file_tableau(name_file, contenu, choix_write):
    file_analyse = open(name_file, choix_write)
    for i in range(len(contenu)):
        file_analyse.write(contenu[i])
    file_analyse.close()

def auto_analyse_full(file):
    # Report + Report Head
    today_date = datetime.now()
    name_file = "Report" + "_" + str(today_date.month) + "-" + str(today_date.day) + \
                "-" + str(today_date.year) + "-" + str(today_date.hour) + \
                ":" + str(today_date.minute) + ".txt"

    # full meta data
    contenu = email_identities.all_meta_data_var(file)
    write_file(name_file, contenu, "a")

    # Short Meta data
    email_identities.short_meta_data_var(file, name_file)

    # body extract
    cont_tab = ["\n==========================",
                "\n[*] Email Body Section [*]",
                "\n==========================",
                "\n\n",
                str(email_identities.body_extract_var(file))]
    write_file_tableau(name_file, cont_tab, "a")
