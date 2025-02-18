import sqlite3
import os



# Fonction pour chercher dans la bdd
def search(val):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Nom FROM Graphes WHERE Nom LIKE ? COLLATE NOCASE", (val + "%",))
    result = cursor.fetchall()
    conn.commit()
    return result

# Fonction pour avoir toutes les informations d'un graphe
def getInfos(Name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Graphes WHERE Nom = ?", (Name,))
    result = cursor.fetchall()
    conn.commit()
    return result