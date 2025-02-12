import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import csv

data1, data2 = [], [] # Listes qui contiendrons les données à extraire
repd1, repd2 = 0, 0 # Réponse pour les données à analyser

def printChooseDico(dict): # Fonction pour afficher clées possibles dictionnaire
    i = 1
    listeChoix = [] # Liste qui contient la valeur des choix possibles
    print("Choisir une clée")
    for key in dict.keys():
        print(f"{i}.{key}")
        i += 1
        listeChoix.append(key)
    return listeChoix

with open('qualite-de-lair-mesuree-dans-la-station-chatelet-rer-a0.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=';')

    for ligne in reader:
        # Permettre à l'utisisateu de faire un choix au premier tour de bouxhe
        while not repd2 in ligne:  # Redemander tant que la réponse 2 n'est pas dans le champ proposé

            listeChoix = printChooseDico(ligne)

            if repd1 in ligne:  # Pour remplir repd1 en premier
                repd2 = int(input())
                if repd2 - 1 in range(len(listeChoix)): # Associer un numéro à une clée
                    repd2 = listeChoix[repd2 - 1] # replacer l'id par le choix
            else:
                repd1 = int(input())
                if repd1 - 1 in range(len(listeChoix)): # Associer un numéro à une clée
                    repd1 = listeChoix[repd1 - 1]  # replacer l'id par le choix


        # Ajouter l'élément
        data1.append(ligne[repd1])
        data2.append(ligne[repd2])


if __name__ == "__main__":
    print(data1, data2)
"""                                                          PARIE 2                                                                   """
# Débogage : Afficher les premières valeurs pour voir le problème
print("Exemples de valeurs de X :", data1[:10])

# Vérifier si data1 contient des dates
date_formats = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S"]
is_date = False
valid_data1 = []  # Liste pour stocker les valeurs correctes

for fmt in date_formats:
    try:
        valid_data1 = [datetime.datetime.strptime(val, fmt) for val in data1]
        is_date = True
        break  # Si un format marche, on arrête la boucle
    except ValueError:
        continue  # Tester le format suivant

# Si ce n'est pas une date, essayer de convertir en nombre
if not is_date:
    try:
        valid_data1 = [float(val) for val in data1]
    except ValueError as e:
        print("Erreur : La colonne sélectionnée pour l'axe X contient des valeurs invalides.")
        print("Valeurs problématiques :", [val for val in data1 if not val.replace('.', '', 1).isdigit()])
        exit()

# Vérifier si data2 est bien numérique
try:
    valid_data2 = [float(val) for val in data2]
except ValueError:
    print("Erreur : La colonne sélectionnée pour l'axe Y contient des valeurs non numériques.")
    exit()

# Débogage : Vérifier le nombre de données retenues
print(f"Nombre de points à tracer : {len(valid_data1)} X {len(valid_data2)}")

# S'assurer qu'il y a des données valides
if not valid_data1 or not valid_data2:
    print("Aucune donnée valide à afficher.")
    exit()

print("Premières valeurs de data1 (X) :", valid_data1[:10])
print("Premières valeurs de data2 (Y) :", valid_data2[:10])
print("Type de data1 :", type(valid_data1[0]) if valid_data1 else "Aucune donnée")
print("Type de data2 :", type(valid_data2[0]) if valid_data2 else "Aucune donnée")

plt.figure(figsize=(10, 5))  # Taille du graphique

# Tracer la courbe
plt.plot(valid_data1, valid_data2, linestyle='-', color='b', label=f"{repd2} en fonction de {repd1}")

# Formatage des axes
plt.xlabel(repd1)
plt.ylabel(repd2)
plt.title(f"Évolution de {repd2} en fonction de {repd1}")
plt.legend()

# Si X est une date, ajuster le format
if is_date:
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45)

# Ajuster l'axe Y de 0 à valeur max
plt.ylim(0, max(valid_data2) * 1.1)  # Ajouter une marge de 10%

plt.grid()
plt.show()
