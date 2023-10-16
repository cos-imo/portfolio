# import des librairies requises
from flask import Blueprint, request, render_template

# Definition du Blueprint
mainBP = Blueprint("mainBP", __name__)


# Status page
@mainBP.route('/status', methods=['GET', 'POST'])
def mainStatus() -> str:
    if request.method == 'GET':
        return "Up and Running!"

@mainBP.route('/display', methods=['GET','POST'])
def display():
    return render_template("display.html")

@mainBP.route('/connexion')
def signin():
    return render_template("signin.html")