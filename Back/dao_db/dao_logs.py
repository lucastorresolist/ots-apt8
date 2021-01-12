import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_log(action:str, type:str) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO logs (action, type) values ('{action}','{type}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_logs():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select data, action, type from logs"
    cursor.execute(sql)
    list_logs = cursor.fetchall()
    return list_logs