from bson import ObjectId
import pymongo


def add_data(coll):
    if coll.find().count() > 0:
        print("Data already inserted")
        return

    print("Adding data")
    book = dict(
        title = "MongoDB Book",
        published = "2013-01-10",
        sold_count = 1
    )
    coll.save(book)

    book = dict(
        title = "MongoDB Book II",
        published = "2014-01-10",
        sold_count = 50
    )
    coll.save(book)

    book = dict(
        title = "Python + Mongo = Love",
        published = "2014-03-10",
        sold_count = 10
    )
    coll.save(book)


def buy_book(books):
    title = 'Python + Mongo = Love'

    books.update({'title': 'Python + Mongo = Love'}, {'$inc': {'sold_count': 1} })
    # the_book = books.find(
    #     {'title': 'Python + Mongo = Love'}
    # )[0]

    #print(the_book)

    #the_book['sold_count'] += 1
    #books.save(the_book)

    the_book = books.find( {'title': 'Python + Mongo = Love'})[0]


    print("The book {} sold {} times".format(
        title, the_book['sold_count']
    ))


def main():
    connection = pymongo.MongoClient()
    db = connection.EsriDemo
    collection = db.Books
    books = collection

    add_data(books)

    buy_book(books)



if __name__ == '__main__':
    main()