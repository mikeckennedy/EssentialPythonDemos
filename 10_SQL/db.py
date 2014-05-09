import os
import sqlite3


def create_connection():
    file = os.path.join('.', 'data', "sample_data.sqlite_db")
    conn = sqlite3.connect(file)
    conn.row_factory = sqlite3.Row
    return conn


def create_schema(conn):
    try:
        print("Creating schema...")
        sql = ( 'create table Authors ' +
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, name text)' )

        conn.execute(sql)

        sql = ('create table Books ' +
               '(id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
               'authorId INTEGER, ' +
               'age INTEGER,' +
               'title text)')

        conn.execute(sql)
    except sqlite3.OperationalError:
        print("Schema already exists...")


def add_data(conn):
    print("Adding data")
    sql = 'SELECT COUNT(*) FROM Books'
    cursor = conn.execute(sql)
    r = cursor.fetchone()
    if r[0]:
        print("already have data, cya")
        return



    sql = 'INSERT INTO Books (authorId, age, title)' \
          'VALUES (7, 42,"Tales from the last century!")'

    conn.execute(sql)

    sql = 'INSERT INTO Books (authorId, age, title)' \
          'VALUES (7, 12,"Tales from the last century! Second Edition")'

    conn.execute(sql)


def find_data(conn, seachtext):
    sql = 'SELECT id, age, title FROM Books WHERE title like ?'

    cursor = conn.execute(sql, ('%'+seachtext+'%',))
    for r in cursor:
        #print(r, type(r))
        print(r, dict(r))
        print(r['id'], r['title'], type(r))


def delete_data(conn):
    return None







