from zfakedata.fakedata import fake
from decouple import config
from dbmodels import Books, Categorys
from fastapi.encoders import jsonable_encoder
from core.engine import SessionLocal


def add_books(amount):
    for i in range(amount):
        
        book = Books(
            store_area=fake.random_storerea(),
            book_name=fake.random_bookname(),
            author=fake.random_author(),
            publication_year=fake.date(),
            publishing_company=fake.random_publishingcompany(),
            sold=False,
            price=fake.random_int()
        )

        categorys = Categorys(title=fake.random_title())

        book.categorys_list.append(categorys)

        with SessionLocal() as session:
            session.add(book)
            session.commit()
            # temp = session.refresh
            # print(jsonable_encoder(temp))
            print("add book Successfully")


add_books(200)
