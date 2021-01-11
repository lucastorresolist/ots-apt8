import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"
def save_category(name:str, phone:str, email:str) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO sellers (name, phone, email) values ('{name}','{phone}','{email}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_sellers():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, phone, email from sellers"
    cursor.execute(sql)
    list_sellers = cursor.fetchall()
    return list_sellers