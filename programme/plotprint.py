from Extractdata import data1, data2, repd1, repd2
import matplotlib.pyplot as plt
import numpy as np

# Fonction pour afficher le graphique en fonction du choix de l'utilisateur
def plot_data(data1, data2, repd1, repd2, plot_type='bar'):
    if len(data1) == 0 or len(data2) == 0:
        print("Aucune donnée à afficher dans le graphique.")
        return
    
    plt.figure(figsize=(10, 6))  # Ajuster la taille de la figure pour plus de clarté
    
    if plot_type == 'bar':
        # Créer un graphique en barres
        plt.bar(data1, data2, width=0.5)  # Utilise les valeurs de data1 pour l'axe x
        plt.xlabel(repd1)  # Nom dynamique de l'axe X
        plt.ylabel(repd2)  # Nom dynamique de l'axe Y
        plt.title(f'Graphique en barres de {repd2} en fonction de {repd1}')
        plt.xticks(rotation=45)  # Rotation pour lisibilité
    
    elif plot_type == 'pie':
        # Créer un graphique circulaire (camembert)
        plt.pie(data2, labels=data1, autopct='%1.1f%%')
        plt.title(f'Répartition de {repd2}')
    
    elif plot_type == 'plot':
        # Créer un graphique en ligne avec marqueurs pour chaque point
        plt.plot(data1, data2, marker='o', linestyle='-', color='b')  
        plt.xlabel(repd1)  
        plt.ylabel(repd2)  
        plt.title(f'Évolution de {repd2} en fonction de {repd1}')
        plt.grid(True)  

    plt.show()

# Exemple d'appel à la fonction avec un menu pour choisir le type de graphique
def main():

    # Générer 5 valeurs arrondies entre le min et le max des données extraites
    data1 = [14, 15, 16, 17, 18]  # Remplace ces valeurs par tes données pour l'axe X
    data2 = [10, 20, 30, 25, 40]  # Remplace ces valeurs par tes données pour l'axe Y
        
    print("Choisissez le type de graphique:")
    print("1 - Barres (bar)")
    print("2 - Camembert (pie)")
    print("3 - Courbe (plot)")
    
    choice = int(input("Entrez votre choix (1, 2 ou 3) : "))
    
    if choice == 1:
        plot_type = 'bar'
    elif choice == 2:
        plot_type = 'pie'
    elif choice == 3:
        plot_type = 'plot'
    else:
        print("Choix invalide. Utilisation du graphique par défaut (bar).")
        plot_type = 'bar'

    plot_data(data1, data2, repd1, repd2, plot_type)

# Lancer le programme
if __name__ == "__main__":
    main()
