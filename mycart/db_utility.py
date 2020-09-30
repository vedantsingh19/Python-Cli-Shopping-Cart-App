import sqlite3
import sys
def make_connection(db):

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    return cursor,connection

