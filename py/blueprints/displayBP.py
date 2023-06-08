# Import des librairies essentielles
from flask import Blueprint, request, render_template

# Import des librairies supplémentaites
from py.database.connectDatabase import connectDatabase

# Definition du Blueprint
displayBP = Blueprint("displayBP", __name__)

@displayBP.route('/display', methods=['GET', 'POST'])
def displayDisplay() -> str:
    if request.method == 'GET':
        return("Everything ok")