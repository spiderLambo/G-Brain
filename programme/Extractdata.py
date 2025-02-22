import csv

data1, data2 = [], [] # Listes qui contiendrons les données à extraire
repd1, repd2 = 0, 0 # Réponse pour les données à analyser


def extractData(filename, param1, param2):
    with open(filename) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        for ligne in reader:
            # permettre le transtypage
            ligne[param1] = ligne[param1].replace(",", ".")
            ligne[param2] = ligne[param2].replace(",", ".")


            # Ajouter l'élément si il peur être convertis
            if ligne[param1].replace(".", "").isdigit() and ligne[param2].replace(".", "").isdigit():
                data2.append(float(ligne[param2]))
                data1.append(float(ligne[param1]))

    return (data1, data2)


# Extrait les colonnes du fichier CSV et les renvoie sous forme de liste.
def extractname(filename):
    with open(filename) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        return list(reader.fieldnames)  # Retourne uniquement les noms des colonnes

