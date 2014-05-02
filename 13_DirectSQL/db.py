import os
import sqlite3


def create_connection():
    current = os.path.abspath('.')
    db_file = os.path.join(current, 'data', 'bookstore.sqlite_db')

    print("Creating connection...")
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn


def create_schema(conn):
    try:
        conn.execute('SELECT * FROM Books')
        print("Table already exists, exiting...")
        return
    except:
        print("Creating table...", end='')

    sql = 'create table Books ' \
          '(id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
          'title text,' \
          'content text,' \
          'view_count INTEGER)'
    conn.execute(sql)
    print("Table created")


def add_some_data(conn):
    with conn:
        print("Adding data... ", end='')

        sql = "SELECT COUNT(*) FROM Books"
        res = conn.execute(sql).fetchone()
        if res[0] > 0:
            print(" data already present.")
            return

        sql = "INSERT INTO Books " \
              "(title, content, view_count) " \
              "VALUES " \
              "('First post from Python', 'some content', 200)"

        conn.execute(sql)

        sql = "INSERT INTO Books " \
              "(title, content, view_count) " \
              "VALUES " \
              "('Second post from Python', 'some content', 10)"

        conn.execute(sql)

    print("done!")


def find_some_data(conn, txt):
    sql = "SElECT id,title,view_count FROM Books " \
          "WHERE title LIKE ?"
    rows = conn.execute(sql, ('%'+txt+'%',))

    for p in rows:
        print("Title = {title}, Count={view_count}".format(
            **dict(p)
        ))

















