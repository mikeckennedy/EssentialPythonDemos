# need engine
# engine is singlton per conn string
import os
import datetime

import sqlalchemy


conn_string = 'sqlite:///' + os.path.join(os.path.abspath('.'), 'data.sqlite_db')
print("Working with db file: ")
print(conn_string)
engine = sqlalchemy.create_engine(conn_string, echo=True)

metadata = sqlalchemy.MetaData(bind=engine)

books = sqlalchemy.Table('Book', metadata,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('title', sqlalchemy.String, nullable=False),
                         sqlalchemy.Column('isbn', sqlalchemy.String),
                         sqlalchemy.Column('copies_sold', sqlalchemy.Integer),
                         sqlalchemy.Column('published', sqlalchemy.DateTime, default=datetime.datetime.now),
)

print("Creating DB...")
metadata.create_all()

print("inserting data...")
# stmt = books.insert().values(
#     title='The first SQLAlchemy book',
#     isbn="83749234987293847",
#     copies_sold=10
# )
# engine.execute(stmt)
# stmt = books.insert().values(
#     title='SQLAlchemy for fun and profit!',
#     isbn="837492349872938423",
#     copies_sold=100
# )
# engine.execute(stmt)
# stmt = books.insert().values(
#     title='More DB with SQLAlchemy',
#     isbn="837492349872933983",
#     copies_sold=0
# )
# engine.execute(stmt)

#print(books.c.title.like('%fun%'))

stmt = books.select().where(True)
cursor = engine.execute(stmt)
for b in cursor:
    print(b.title, b.copies_sold + 1)

stmt = books.update() \
    .where(books.c.isbn == "83749234987293847") \
    .values(copies_sold=20)

engine.execute(stmt)


stmt = books.delete() \
    .where(books.c.isbn == "83749234987293847")

engine.execute(stmt)











