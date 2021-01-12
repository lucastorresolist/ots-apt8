import psycopg2
from Back.models.seller import Seller


_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"


def save_seller(seller:Seller) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO sellers (name, phone, email) values ('{seller.name}','{seller.phone}','{seller.email}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def list_sellers():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, phone, email, id from sellers"
    cursor.execute(sql)
    result = cursor.fetchall()
    sellers = []
    for item in result:
        seller = Seller(item[0], item[1], item[2], item[3])
        sellers.append(seller)
    return sellers
