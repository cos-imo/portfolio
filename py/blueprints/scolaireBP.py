# Import des librairies essentielles
from flask import Blueprint, request, render_template

# Definition du Blueprint
scolaireBP = Blueprint("scolaireBP", __name__)

@scolaireBP.route('/scolaire', methods=['GET', 'POST'])
def afficherScolaire() -> str:
    if request.method == 'GET':
        return render_template("scolaire.html")
    
@scolaireBP.route('/projet', methods=['GET', 'POST'])
def afficherProjetVide() -> str:
    if request.method == 'GET':
        return render_template("projet.html")