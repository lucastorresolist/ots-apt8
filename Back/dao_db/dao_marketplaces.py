import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_marketplace(name:str, description:str) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO marketplaces (name, description) values ('{name}','{description}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_mkplaces():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, description from marketplaces"
    cursor.execute(sql)
    list_mkplaces = cursor.fetchall()
    return list_mkplaces