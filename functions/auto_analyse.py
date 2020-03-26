""""
	Auteur : Julien Michelet et Philippe-Alexandre Munch
	Date : mars 2020
	But du programme :
	Fonction automatique des fonctions suivantes :

	Version : 1.0
"""

from datetime import datetime
from functions import email_identities
from functions.functions_basique import search_word_add_string, read_file,write_file, write_file_tableau,read_file_write_report


def auto_analyse_full(file):
    # Report + Report Head
    day_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    today_date = datetime.now()
    name_file = "Report" + "_" + str(today_date.day) + "-" + str(today_date.month) + \
                "-" + str(today_date.year) + "-" + str(today_date.hour) + \
                ":" + str(today_date.minute) + ".txt"

        # Report Header, creation ou suppression du fichier existant
    read_file_write_report("./graphical/report_header.py", name_file, "w")
    contenu = search_word_add_string(str(read_file(name_file)), "Report:", name_file)
    contenu = search_word_add_string(contenu, "Date:", day_date)
    write_file(name_file, contenu, "w")

        # full meta data - pas d'utilité à voir plus tard
    # contenu = email_identities.all_meta_data_var(file)
    # write_file(name_file, contenu, "a")

        # Short Meta data
    contenu = email_identities.short_meta_data_var(file)
    write_file_tableau(name_file, contenu, "a")
    contenu = search_word_add_string(str(read_file(name_file)), "1)", "Short Meta Data : OK")
    write_file(name_file, contenu, "w")
    print("Short Meta Data : OK")
        # body extract
    cont_tab = ["\n==========================",
                "\n[*] Email Body Section [*]",
                "\n==========================",
                "\n\n",
                str(email_identities.body_extract_var(file))]
    write_file_tableau(name_file, cont_tab, "a")
    contenu = search_word_add_string(str(read_file(name_file)), "2)", "Body Extract    : OK")
    write_file(name_file, contenu, "w")
    print("Body Extract    : OK")
