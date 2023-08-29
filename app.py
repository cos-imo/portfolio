# import des librairies essentielles
from flask import Flask, flash, redirect


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