import os
from flask import Flask, render_template, request, redirect, session
from bddGestion import *
from programme.Extractdata import extractname

# Création de l'application
app = Flask(__name__, static_url_path="/static")
app.secret_key = "supersecretkey"  # Nécessaire pour utiliser `session`


# Page principale
@app.route("/", methods=["GET", "POST"])  # Présision du chemin
def home():
    # Envois de la recherche
    if request.method == "POST":
        action = request.form  # Récupérer les données du formulaire

        return redirect(f"/search/{action.get('rechercher')}")  # Rediriger

    return render_template("g-brain_principal.html")


# Page de recherche
@app.route("/search/<recherche>", methods=["GET", "POST"])
def searchapp(recherche):
    # Envois de la recherche
    if request.method == "POST":
        action = request.form  # Récupérer les données du formulaire

        return redirect(f"/search/{action.get('rechercher')}")  # Rediriger

    # Envoyer la page avec la recherche
    return render_template("g-brain_recherche.html", search=search(recherche))

# Page d'un graphique
@app.route("/graph/<graphName>")
def graph(graphName):
    infos = getInfos((graphName))

    if infos == []: # Si le document n'existe pas
        infos = [('Graphique Inconnu', '', '', '')]

    return render_template("g-brain_graphe.html", info = infos)


# Page de connexion
@app.route("/connexion", methods=["GET", "POST"])
def connect():
    # Renvoie une page en fonction de l'utilisateur
    if isin((request.args.get("Nom"), request.args.get("Pass"))) or session.get("fichierEnregistre"):
        # Marquer le fichier comme enregistré
        session["fichierEnregistre"] = True

        fichier = request.files.get("file")  # Récupérer le fichier
        if request.method == "POST":
            if fichier:
                file_path = os.path.join("uploads", fichier.filename)
                fichier.save(file_path)  # Sauvegarde temporaire

                session["file_path"] = file_path  # On stocke le chemin du fichier

            return redirect("/choisirParametre")
        return render_template("g-brain_ajout.html")
    else:
        return render_template('g-brain_connexion.html')


@app.route("/choisirParametre")
def param():
    return session["file_path"]


# Page d'erreur
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)  # Lancement de l'application
