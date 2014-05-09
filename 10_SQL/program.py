import db


with db.create_connection() as conn:
    db.create_schema(conn)
    db.add_data(conn)
    txt = input("What do you want to search for? ")
    db.find_data(conn, txt)
    db.delete_data(conn)