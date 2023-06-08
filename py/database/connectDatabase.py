# Import des librairies essentielles
import sqlite3

def connectDatabase():
    db = sqlite3.connect('short_urls.db')
    cursor = db.cursor()
    return db, cursor