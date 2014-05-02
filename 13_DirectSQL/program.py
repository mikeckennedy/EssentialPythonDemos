import db


def main():
    conn = db.create_connection()
    db.create_schema(conn)
    db.add_some_data(conn)
    txt = input("Enter a keyword. ")
    db.find_some_data(conn, txt)



if __name__ == '__main__':
    main()