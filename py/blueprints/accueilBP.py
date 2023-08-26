# Import des librairies essentielles
from flask import Blueprint, request, render_template

# Definition du Blueprint
accueilBP = Blueprint("accueilBP", __name__)

@accueilBP.route('/', methods=['GET', 'POST'])
def displayPersonnel() -> str:
    if request.method == 'GET':
        return render_template("jumbotron.html")