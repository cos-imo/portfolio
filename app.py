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
    if request.method == 'POST' and request.form.get('identifiant') and request.form.get('password'):
        r = sqlite3.connect(DATABASE).cursor()
        nom = request.form.get('identifiant')
        mdp = bytes(request.form.get('password'), 'utf-8')
        mass = hashlib.sha256(mdp).hexdigest()
        r.execute("SELECT motdepasse FROM utilisateurs WHERE identifiant=?", (nom,))
        tuple = r.fetchall()
        if not tuple:
            tuple=[[""]]
        if tuple[0][0] == mass:
            print("Connection succeeded")
    return render_template("signin.html")
