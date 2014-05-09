import os
import datetime

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative


conn_string = 'sqlite:///' + os.path.join(os.path.abspath('.'), 'data_orm.sqlite_db')
print("Working with db file: ")
print(conn_string)
engine = sqlalchemy.create_engine(conn_string, echo=True)

EntityBase = sqlalchemy.ext.declarative.declarative_base(bind=engine)
session_factory = sqlalchemy.orm.sessionmaker(bind=engine)


class Book(EntityBase):
    __tablename__ = "Book"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    isbn = sqlalchemy.Column(sqlalchemy.String)
    copies_sold = sqlalchemy.Column(sqlalchemy.Integer)
    published = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    author = sqlalchemy.orm.relationship("Author")
    author_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Author.id"))


class Author(EntityBase):
    __tablename__ = "Author"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    books = sqlalchemy.orm.relationship("Book")

print("Creating tables")
EntityBase.metadata.create_all()

print("Inserting data...")

session = session_factory()

num_of_books = session.query(Book).filter(Book.copies_sold > 0).count()
print(num_of_books)

if not num_of_books:
    # do work
    print("Adding data")

    a = Author()
    a.name = "Ted"
    session.add(a)

    b = Book()
    b.title = "First book"
    b.isbn = "1283908wq98089"
    b.author = a
    session.add(b)
    b = Book()
    b.title = "Second book"
    b.isbn = "23423749"
    b.copies_sold = 10
    b.author = a
    session.add(b)
    b = Book()
    b.title = "Third book"
    b.isbn = "39849308409839"
    b.copies_sold = 20
    b.author = a
    session.add(b)
    session.commit()
else:
    print("Data already there.")


session = session_factory()
print("Here are our books:")
q = session.query(Book)
for b in q[:2]:
    print(b.title, b.isbn, b.copies_sold, type(b))
print()
isbn = "23423749"#input("Which one do you want (ISBN PLEASE): ")

book = session.query(Book).filter(Book.isbn == isbn).one()
print("You mean: " + book.title + "?")

book.copies_sold += 1

session.commit()


session = session_factory()
print("Books that have sold:")
q = session.query(Book)\
    .filter( Book.title.startswith("Second"))\
    .order_by(Book.copies_sold.desc())

for b in q:
    print(b.title, b.isbn, b.copies_sold, type(b))
print()


print("Author")
session = session_factory()
a = session.query(Author).options(sqlalchemy.orm.joinedload(Author.books)).one()
print("Found author: " + str(a))
print("Finding books")
for b in a.books:
    print(b)

















