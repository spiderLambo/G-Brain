import csv

data1, data2 = [], []

with open('qualite-de-lair-mesuree-dans-la-station-chatelet-rer-a0.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=';')
    for ligne in reader:
        data1.append(ligne["\ufeffdate/heure"])
        data2.append(ligne["TEMP"])


if __name__ == "__main__":
    print(data1, data2)