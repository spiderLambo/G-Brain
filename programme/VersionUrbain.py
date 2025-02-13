from Extractdata import data1, data2
import matplotlib.pyplot as plt

# Fonction pour afficher le graphique en fonction du choix de l'utilisateur
def plot_data(data1, data2, plot_type='bar'):
    if len(data1) == 0 or len(data2) == 0:
        print("Aucune donnée à afficher dans le graphique.")
        return
    
    plt.figure(figsize=(10, 6))  # Ajuster la taille de la figure pour plus de clarté
    
    if plot_type == 'bar':
        # Créer un graphique en barres
        plt.bar(data1, data2, width=0.5)  # Utilise les valeurs de data1 pour l'axe x
        plt.xlabel('Valeur mesurée')  # Description de l'axe X
        plt.ylabel('Qualité de l\'air (µg/m³)')  # Description de l'axe Y
        plt.title('Variation de la qualité de l\'air en fonction de la valeur mesurée')  # Titre du graphique
        plt.xticks(rotation=45)  # Ajouter une rotation aux étiquettes sur l'axe X pour plus de lisibilité
    
    elif plot_type == 'pie':
        # Créer un graphique circulaire (camembert)
        plt.pie(data2, labels=data1, autopct='%1.1f%%')
        plt.title('Répartition de la qualité de l\'air')  # Titre du graphique
    
    elif plot_type == 'plot':
        # Créer un graphique en ligne (plot) avec marqueurs pour chaque point
        plt.plot(data1, data2, marker='o', linestyle='-', color='b')  # Utilise les valeurs de data1 pour l'axe X
        plt.xlabel('Valeur mesurée')  # Description de l'axe X
        plt.ylabel('Qualité de l\'air (µg/m³)')  # Description de l'axe Y
        plt.title('Évolution de la qualité de l\'air dans le temps')  # Titre du graphique
        plt.grid(True)  # Ajouter une grille pour améliorer la lisibilité

    plt.show()

# Exemple d'appel à la fonction avec un menu pour choisir le type de graphique
def main():
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

    plot_data(data1, data2, plot_type)

# Lancer le programme
if __name__ == "__main__":
    main()