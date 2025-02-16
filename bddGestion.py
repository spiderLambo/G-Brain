import sqlite3

# Fonction pour chercher dans la bdd
def search(val):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT Nom FROM Graphes WHERE Nom LIKE '{val}%'")
    result = cursor.fetchall()
    conn.commit()
    return result