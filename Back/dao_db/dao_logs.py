from Back.models.log import Log
import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"


def save_log(log: Log) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO logs (action, type) VALUES ('{log.action}','{log.type}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_logs():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "SELECT id, data, action, type FROM logs"
    cursor.execute(sql)
    result = cursor.fetchall()
    list_logs = []
    for item in result:
        log = Log(item[2], item[3], item[1], item[0])
        print(log.action, log.data)
        list_logs.append(log)
    return list_logs
