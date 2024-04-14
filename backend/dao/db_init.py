import sqlite3
import os

def startup():
    if os.path.isfile("db.sqlite3") is False:

        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()

        sql = "Create table events (event_id, event_name, user_id, start_time, end_time, is_deleted)"
        cur.execute(sql)
        sql = "Create table users (user_id, email, password_hash, is_active)"
        cur.execute(sql)


        con.commit()

    else:
        print("DB already initt'ed")
