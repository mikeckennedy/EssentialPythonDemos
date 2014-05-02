from db import DB


def main():
    db = DB()
    db.add_data()
    db.find_data()
    db.delete_some_data()
    db.find_data()



if __name__ == '__main__':
    main()