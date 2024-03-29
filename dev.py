# import des librairies essentielles
from flask import Flask, flash, redirect



def createApp() -> None:
    app = Flask(__name__)


    app.config['SECRET_KEY'] = '1sZn3QAl35qIYaoqjLbB9JxuYxqOyVN3'


    # Import blueprints
    ## Import main blueprint
    from py.blueprints.mainBP import mainBP
    app.register_blueprint(mainBP)

    ## Import display blueprint
    from py.blueprints.displayBP import displayBP
    app.register_blueprint(displayBP)

    from py.blueprints.headersBP import headersBP
    app.register_blueprint(headersBP)

    
    # Error 404 handler
    @app.errorhandler(404)
    def pageNotFound(error):
        return redirect('/')

    return app



if __name__ == "__main__":
    app = createApp()
    app.run(debug=1, host='0.0.0.0', port='5454')