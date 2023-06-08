# Import des librairies essentielles
from flask import Blueprint, request, render_template

# Definition du Blueprint
liensBP = Blueprint("liensBP", __name__)

@liensBP.route('/liens', methods=['GET', 'POST'])
def displayliens() -> str:
    if request.method == 'GET':
        return render_template("liens.html")