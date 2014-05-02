import os
import datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String, Date


class DB:

    def __init__(self):
        conn_str = self.get_conn_string()
        
        self.engine = sqlalchemy.create_engine(conn_str, echo=True)
        self.metadata = sqlalchemy.MetaData(bind=self.engine)
        
        self.build_metadata(self.metadata)
        
    def get_conn_string(self):
        file = os.path.join(
            os.path.abspath('.'),
            'data',
            'sql_alc.sqlite_db'
        )
        conn_str = 'sqlite:///' + file
        #print(conn_str)
        return conn_str

    def build_metadata(self, metadata):
        self.books = sqlalchemy.Table(
            'Books', metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String, nullable=False),
            Column('content', String),
            Column('published', Date, default=datetime.datetime.now),
            Column('copies_sold', Integer)
        )

        metadata.create_all()

    def add_data(self):

        q = self.books.select().count()
        c = self.engine.execute(q).fetchone()[0]
        print("There are currently {0} books".format(c))
        if c > 0:
            return

        s = self.books.insert().values(
            title="First Post from SQLAlchemy",
            copies_sold=0
        )
        self.engine.execute(s)
        s = self.books.insert().values(
            title="SQLAlchemy core and beyond",
            copies_sold=10
        )
        self.engine.execute(s)
        s = self.books.insert().values(
            title="SQLAlchemy cookbook",
            copies_sold=20
        )
        self.engine.execute(s)

    def find_data(self):
        print("Expression="+str(self.books.c.title.like("%cookbook%")))
        s = self.books.select().where(
            self.books.c.copies_sold > 0
        )

        print("Find a book")
        res = self.engine.execute(s)
        for b in res:
            print(b)

    def delete_some_data(self):
        s = self.books.delete().where(self.books.c.copies_sold >10)
        self.engine.execute(s)
        print("DELETE!!!!!!!!!!!!!!!!")