from flask import Blueprint, request, render_template, url_for

from py.database.connectDatabase import connectDatabase

headersBP = Blueprint("headersBP", __name__)

@headersBP.route('/headers', methods=['GET','POST'])
def display():
    return render_template("headerstest.html")
