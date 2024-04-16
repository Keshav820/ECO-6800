import sqlite3
import os

def startup():
    if os.path.isfile("db.sqlite3") is False:

        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()

        sql = "CREATE TABLE events (event_id PRIMARY KEY, event_name TEXT NOT NULL, user_id TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, is_deleted INT)"
        cur.execute(sql)
        sql = "Create table users (user_id PRIMARY KEY, email, password_hash, is_active)"
        cur.execute(sql)
        sql = "Create table contacts (owner_id, user_id, PRIMARY KEY(owner_id, user_id))"
        cur.execute(sql)


        con.commit()

    else:
        print("DB already initt'ed")
