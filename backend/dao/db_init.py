import sqlite3
import os

def startup():
    if os.path.isfile("db.sqlite3") is False:

        cnx = sqlite3.connect("db.sqlite3")
        cur = cnx.cursor()

    else:
        print("DB already initt'ed")
