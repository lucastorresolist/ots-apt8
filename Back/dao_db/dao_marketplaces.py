import psycopg2
from Back.models.marketplace import Marketplace


_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"


def save_mkplace(marketplace:Marketplace) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO marketplaces (name, description) values ('{marketplace.name}','{marketplace.description}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def list_mkplaces():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, description, id from marketplaces"
    cursor.execute(sql)
    result = cursor.fetchall()
    marketplaces = []
    for item in result:
        marketplace = Marketplace(item[0], item[1], item[2])
        marketplaces.append(marketplace)
    return marketplaces
