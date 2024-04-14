import sqlite3

def validate_token(token: str):
    cnx = sqlite3.connect("db.sqlite3")
    cur = cnx.cursor()

    sql = "select cast(user_id as text) from users where password_hash = ? and is_active=1"
    cur.execute(sql, (token,))

    result = cur.fetchone()[0]

    return result