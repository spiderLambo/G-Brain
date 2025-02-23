import matplotlib.pyplot as plt
import numpy as np

# Fonction pour afficher le graphique en fonction du choix de l'utilisateur
def plot_data(data1, data2, repd1, repd2, fichier_nom):
    if len(data1) == 0 or len(data2) == 0:
        print("Aucune donnée à afficher dans le graphique.")
        return
    
    plt.figure(figsize=(10, 6))  # Ajuster la taille de la figure pour plus de clarté


    # Créer un graphique en barres
    plt.bar(data1, data2, width=0.5)  # Utilise les valeurs de data1 pour l'axe x
    plt.xlabel(repd1)  # Nom dynamique de l'axe X
    plt.ylabel(repd2)  # Nom dynamique de l'axe Y
    plt.title(f'Graphique en barres de {repd2} en fonction de {repd1}')
    plt.xticks(rotation=45)  # Rotation pour lisibilité

    plt.savefig(f"static/graphs/bar/{fichier_nom}.png")


    # Créer un graphique en nuages de points
    plt.scatter(data1, data2, s=1)
    plt.xlabel(repd1)  # Nom dynamique de l'axe X
    plt.ylabel(repd2)  # Nom dynamique de l'axe Y
    plt.title(f'Nuages de points de {repd2} en fonction de {repd1}')

    plt.savefig(f"static/graphs/scatter/{fichier_nom}.png")

    # Créer un graphique en ligne
    plt.plot(data1, data2, marker='o', linestyle='-', color='b')
    plt.xlabel(repd1)
    plt.ylabel(repd2)
    plt.title(f'Évolution de {repd2} en fonction de {repd1}')
    plt.grid(True)

    plt.savefig(f"static/graphs/plot/{fichier_nom}.png")


