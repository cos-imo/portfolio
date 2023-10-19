# import des librairies requises
from flask import Blueprint, request, render_template
import sqlite3

# Definition du Blueprint
mainBP = Blueprint("mainBP", __name__)
