import sqlite3
from classes.request import Event

def persist_event(request: Event):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    sql = "insert into events (event_id, event_name, user_id, start_time, end_time, is_deleted) values (?, ?, ?, ?, ?, 0) on conflict(event_id) do update set event_name=?, start_time=?, end_time=?"

    cur.execute(sql, (request.event_id, request.event_name, request.created_by, request.start_time, request.end_time, request.event_name, request.start_time, request.end_time))
    con.commit()

def get_events_self(user_id:str):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    sql = "select event_id, event_name, user_id, start_time, end_time from events where user_id =? and is_deleted=0"

    cur.execute(sql, (user_id,))
    result_set = cur.fetchall()

    return [Event(*row) for row in result_set]

def get_events_self_event_id(user_id:str, event_id:str):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    sql = "select event_id, event_name, user_id, start_time, end_time from events where user_id =? and event_id=? and is_deleted=0 limit 1"

    try:
        cur.execute(sql, (user_id, event_id,))
        result_set = cur.fetchall()

        if not result_set:
            raise Exception
        else:
            res = [Event(*row) for row in result_set]
    except Exception as e:
        raise ValueError("No such event for this user_id")
    return res[0]

def delete_event(user_id:str, event_id:str):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    sql = "update events set is_deleted=1 where user_id=? and event_id=?"
    cur.execute(sql, (user_id, event_id))
    con.commit()