data1, data2 = [], [] # Listes qui contiendrons les valeus qui seron extraites

def sameind(text, val): # fonction pour savoir l'indice d'une valeur recherchée
    listind = []
    for i in range(len(text)):
        if text[i] == val:
            listind.append(i)
    return listind

with open("qualite-de-lair-mesuree-dans-la-station-chatelet-rer-a0.csv") as f: #ouverture du fichier csv
    for line in f.readlines(): # Parcour de chaque ligne
        listind = sameind(line, ";") # liste d'indices des caractères qui sont : ;
        data1.append(line[:listind[0]])
        data2.append(line[listind[1]+1:listind[2]])

print(data1, data2)