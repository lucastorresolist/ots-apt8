import psycopg2


def credentials():
    _host = 'pgsql08-farm15.uni5.net'
    _user = 'topskills13'
    _password = 'olist123'
    _database = 'topskills13'
    connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"
    return connection_string
