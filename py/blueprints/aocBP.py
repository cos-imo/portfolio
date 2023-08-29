
from flask import Blueprint, request, render_template, url_for

adventofcodeBP = Blueprint("aocBP", __name__)

@adventofcodeBP.route('/adventofcode', methods=['GET','POST'])
def display():
    return render_template("advent_of_code.html")