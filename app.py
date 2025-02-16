from flask import Flask, render_template

# Création de l'application
app = Flask(__name__, static_url_path="/static")


@app.route("/") # Présision du chemin
def home():
    return render_template('g-brain_principal.html')




if __name__ == "__main__":
    app.run(debug=True) # Lancement de l'application