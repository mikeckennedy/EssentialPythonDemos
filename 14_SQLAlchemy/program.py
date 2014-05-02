from db import DB
from db_orm import DBORM


def main():
    # db = DB()
    # db.add_data()
    # db.find_data()
    # db.delete_some_data()
    # db.find_data()

    db = DBORM()
    db.add_some_data()
    db.show_data()



if __name__ == '__main__':
    main()