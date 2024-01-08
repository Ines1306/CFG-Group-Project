import json
import mysql.connector


class DbConnectionError(Exception):
    pass


# Connecting to our DB thrilltopia
with open('config.json') as config_file:
    config = json.load(config_file)

# Access specific configuration values
db_config = config['database']
db_host = db_config['host']
db_user = db_config['user']
db_password = db_config['password']
db_name = db_config['database_name']


def connect_to_db(db_name):
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        auth_plugin='mysql_native_password'
    )
    return conn
