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
report_date = "\nDATE: ", str(today_date.month) + str(today_date.day) + str(today_date.year)\
              + str(today_date.hour) + str(today_date.minute)


def auto_analyse_full(file):
    # Report + Report Head
    today_date = datetime.now()
    name_file = "Report" + "_" + str(today_date.month) + "-" + str(today_date.day) +\
                "-" + str(today_date.year) + "-" + str(today_date.hour) +\
                ":" + str(today_date.minute) + ".txt"

    # full meta data
    contenu = email_identities.all_meta_data_var(file)
    file_analyse = open(name_file, "a")
    file_analyse.write(contenu)
    file_analyse.close()

    # Short Meta data
    email_identities.short_meta_data_var(file, name_file)

    # body extract
    file_analyse = open(name_file, "a")
    file_analyse.write("\n==========================")
    file_analyse.write("\n[*] Email Body Section [*]")
    file_analyse.write("\n==========================")
    file_analyse.write("\n")
    file_analyse.write(str(email_identities.body_extract_var(file)))
    file_analyse.close()


