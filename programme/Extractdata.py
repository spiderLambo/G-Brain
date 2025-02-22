import csv
import datetime

data1, data2 = [], [] # Listes qui contiendrons les données à extraire
repd1, repd2 = 0, 0 # Réponse pour les données à analyser


def extractData(filename, param1, param2):
    with open(filename) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        for ligne in reader:
            # permettre le transtypage
            ligne[param1] = ligne[param1].replace(",", ".")
            ligne[param2] = ligne[param2].replace(",", ".")


            # Ajouter l'élément si il s'agit de deux réels
            if ligne[param1].replace(".", "").isdigit() and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(float(ligne[param1]))

            # Ajouter l'élément si il s'agit d'un réel et une date au format 2025-01-01
            elif "-" in ligne[param1] and len(ligne[param1]) == 10 and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(datetime.datetime.strptime(ligne[param1], "%Y-%m-%d"))

            # Ajouter l'élément si il s'agit d'un réel et une date au format 01/01/2025
            elif "/" in ligne[param1] and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(datetime.datetime.strptime(ligne[param1], "%d/%m/%Y"))

            # Ajouter l'élément si il s'agit d'un réel et une date au format January 1, 2025
            elif "," in ligne[param1] and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(datetime.datetime.strptime(ligne[param1], "%B %d, %Y"))

            # Ajouter l'élément si il s'agit d'un réel et une date au format 01-01-2025 00:00
            elif "-" in ligne[param1] and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(datetime.datetime.strptime(ligne[param1], "%d-%m-%Y %H:%M"))


    return (data1, data2)


# Extrait les colonnes du fichier CSV et les renvoie sous forme de liste.
def extractname(filename):
    with open(filename) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        return list(reader.fieldnames)  # Retourne uniquement les noms des colonnes

