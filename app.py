from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des tâches (simples données en mémoire pour cette démo)
taches = []

@app.route("/")
def index():
    return render_template("index.html", taches=taches)

@app.route("/ajouter", methods=["POST"])
def ajouter_tache():
    tache = request.form.get("tache")
    if tache:
        taches.append({"tache": tache, "terminee": False})
    return redirect(url_for("index"))

@app.route("/terminer/<int:index>")
def terminer_tache(index):
    if 0 <= index < len(taches):
        taches[index]["terminee"] = True
    return redirect(url_for("index"))

@app.route("/supprimer/<int:index>")
def supprimer_tache(index):
    if 0 <= index < len(taches):
        taches.pop(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
