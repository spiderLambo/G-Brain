import sqlite3

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

# Fonction pour déterminer si un utilisateur est dans la bdd
def isin(tuple):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Admins WHERE Nom = ? AND Pass = ?", tuple)
    result = cursor.fetchall()
    conn.commit()
    return not result ==[]


# Fonction pour ajouter un graphe
def addGraph(nom, bar, scatter, plot):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Graphes VALUES (?, ?, ?, ?)", (nom, bar, scatter, plot))
    conn.commit()
    conn.close()