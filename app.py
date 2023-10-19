# import des librairies essentielles
from flask import Flask, flash, redirect, request, render_template
import sqlite3, hashlib


app = Flask(__name__)

app.config['SECRET_KEY'] = '1sZn3QAl35qIYaoqjLbB9JxuYxqOyVN3'

# Import blueprints
## Import main blueprint
from py.blueprints.mainBP import mainBP
app.register_blueprint(mainBP)
## Import blueprint "personnel"
from py.blueprints.personnelBP import personnelBP
app.register_blueprint(personnelBP)
## Import blueprint "scolaire"
from py.blueprints.scolaireBP import scolaireBP
app.register_blueprint(scolaireBP)
## Import blueprint "accueil"
from py.blueprints.accueilBP import accueilBP
app.register_blueprint(accueilBP)
## Import blueprint "About"
from py.blueprints.liensBP import liensBP
app.register_blueprint(liensBP)
## Import headers blueprint
from py.blueprints.headersBP import headersBP
app.register_blueprint(headersBP)
## Import advent of code blueprint
from py.blueprints.aocBP import adventofcodeBP
app.register_blueprint(adventofcodeBP)


# Error 404 handler
@app.errorhandler(404)
def pageNotFound(error):
    return redirect('/')

DATABASE = 'project.db'

DATABASE = 'project.db'
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "anystringhere"


def get_db():
    return sqlite3.connect(DATABASE)

# Fermeture de la DB


@app.teardown_appcontext
def close_connection(exception):
    get_db().close()

@app.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    # Si le formulaire est bien rempli...
    if request.method == 'POST' and request.form.get('identifiant') and request.form.get('password'):
        print("connexion")
        r = get_db().cursor()  # On créé un curseur
        nom = request.form.get('name')  # On récupère les données du formulaire
        mdp = bytes(request.form.get('password'), 'utf-8')
        # On calcule le hash du mot de passe entré
        mass = hashlib.sha256(mdp).hexdigest()
        # On récupère le hash de l'identifiant entré
        r.execute("SELECT motdepasse FROM utilisateurs WHERE identifiant=?", (nom,))
        tuple = r.fetchall()
        if not tuple:
            tuple=[[""]]
        if tuple[0][0] == mass:  # Si les deux correspondent...
            r = get_db().cursor()
            r.execute("SELECT id FROM utilisateurs WHERE pseudo=?",
                      (nom,))  # On récupère l'id
            tuple = r.fetchall()[0][0]
            session["id_utilisateur"] = tuple  # Et on le stocke dans session
            rsession = get_db().cursor()
            rsession.execute("SELECT statut FROM utilisateurs WHERE id={}".format(  # On récupère le statut (utilisateur ou producteur)
                session["id_utilisateur"]))
            session_type = rsession.fetchall()[0][0]
            return render_template('signin.html')
        else:
            print("Connection failed")
    # Si rien ne se passe (ou erreur) on recharge la même page
    return render_template("signin.html")
