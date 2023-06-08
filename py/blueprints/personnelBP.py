# Import des librairies essentielles
from flask import Blueprint, request, render_template

# Definition du Blueprint
personnelBP = Blueprint("personnelBP", __name__)

@personnelBP.route('/personnel', methods=['GET', 'POST'])
def displayPersonnel() -> str:
    if request.method == 'GET':
        return render_template("personnel.html")