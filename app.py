from flask import Flask, render_template, request, redirect
from bddGestion import *

# Création de l'application
app = Flask(__name__, static_url_path="/static")


# Page principale
@app.route("/", methods=["GET", "POST"])  # Présision du chemin
def home():
    # Envois de la recherche
    if request.method == "POST":
        action = request.form  # Récupérer les données du formulaire

        return redirect(f"/search/{action.get('rechercher')}")  # Rediriger

    return render_template("g-brain_principal.html")


# Page de recherche
@app.route("/search/<recherche>")
def searchapp(recherche):
    return render_template("g-brain_recherche.html", search=search(recherche))


if __name__ == "__main__":
    app.run(debug=True)  # Lancement de l'application
