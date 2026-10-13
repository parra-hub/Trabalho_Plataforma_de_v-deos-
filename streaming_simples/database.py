import mysql.connector
from flask import g


def get_connection():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='99802@Gabi',
            database='streaming_novo'
        )
    return g.db


def close_connection(error=None):
    if 'db' in g:
        g.db.close()
