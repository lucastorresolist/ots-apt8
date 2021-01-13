from .connection import *
from Back.models.model_logs import Log


def save_log(log: Log) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO logs (action, type) VALUES ('{log.action}','{log.type}')"
        cursor.execute(sql)
        conn.commit()

def list_logs():
    list_logs = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "SELECT id, data, action, type FROM logs"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            log = Log(item[2], item[3], item[1], item[0])
            list_logs.append(log)
    return list_logs
