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


@mainBP.route("/connexion", methods=['GET', 'POST'])
def connexion_page():
    if request.method == 'POST' and request.form.get('identifiant') and request.form.get('password'):
        r = get_db().cursor()
        nom = request.form.get('identifiant')
        mdp = bytes(request.form.get('password'), 'utf-8')
        mass = hashlib.sha256(mdp).hexdigest()
        r.execute("SELECT motdepasse FROM utilisateurs WHERE pseudo=?", (nom,))
        tuple = r.fetchall()
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
            if session_type == 1:
                # On renvoie ensuite la page correspondante
                return redirect(url_for("renvoyer_dashboard_util"))
            elif session_type == 2:
                # On renvoie ensuite la page correspondante
                return redirect(url_for("renvoyer_prod"))
            print("connected")

            return redirect(url_for("renvoyer_dashboard_util"))
        else:
            print("Connection failed")
    # Si rien ne se passe (ou erreur) on recharge la même page
    return render_template("connexion.html")