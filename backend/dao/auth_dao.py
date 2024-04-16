import sqlite3

def validate_token(token: str):
    cnx = sqlite3.connect("db.sqlite3")
    cur = cnx.cursor()

    sql = "select user_id from users where password_hash = ? and is_active=1"
    cur.execute(sql, (token,))

    result = cur.fetchone()[0]

    return result

def is_user_in_contact_list(user_id: str, owner_id:str):
    cnx = sqlite3.connect("db.sqlite3")
    cur = cnx.cursor()

    sql = "select 1 from contacts where owner_id = ? and user_id=?"
    cur.execute(sql, (owner_id, user_id))

    result = cur.fetchone()[0]

    if result is not None:
        return True
    else:
        return False