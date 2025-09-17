
# flask est un framework léger pour développer des applications Web à l'aide du langage de programmation Python.Il a été créé par Armin Ronacher et lancé en 2010, gagnant rapidement en popularité parmi ceux qui recherchent une alternative plus simple et plus flexible à Django pour créer toutes sortes d'applications Web.
from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # mon fichier HTML

@app.route("/cv")
def download_cv():
    return send_file("MonCV.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
