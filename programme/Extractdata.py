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

with open('vacsi12-dep-2022-01-26-19h10.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=';')
    i=0
    for ligne in reader:
        # Permettre à l'utisisateur de faire un choix au premier tour de bouxhe
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

        # permettre le transtypage
        ligne[repd1] = ligne[repd1].replace(",", ".")
        ligne[repd2] = ligne[repd2].replace(",", ".")


        # Ajouter l'élément si il peur être convertis
        if ligne[repd1].replace(".", "").isdigit() and ligne[repd2].replace(".", "").isdigit():
            data2.append(float(ligne[repd2]))
            data1.append(float(ligne[repd1]))


if __name__ == "__main__":
    print("data1:", len(data1))
    print("data2:", len(data2))