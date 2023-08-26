from flask import Blueprint, request, render_template, url_for

from py.database.connectDatabase import connectDatabase

headersBP = Blueprint("headersBP", __name__)

@headersBP.route('/headers', methods=['GET','POST'])
def display():
    return render_template("headerstest.html")

@headersBP.route("/bootstrap-css.css")
def bootstrap_css():
    return url_for('static',"css/bootstrap-css.css")

@headersBP.route("/headers.css")
def headers_css():
    return url_for('static',"css/headers.css")

@headersBP.route("/bootstrap.min.css")
def boostrapmincss():
    return url_for('static',"css/bootstrap.min.css")