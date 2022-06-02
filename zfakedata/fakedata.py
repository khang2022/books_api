import random
from faker import Faker
from faker.providers import BaseProvider
import json


with open('F:/book_project/app/zfakedata/fakedata.json') as f:
    data = json.load(f)


fake = Faker()


class Book_Info(BaseProvider):

    bookname_list = data["bookname"]
    author_list = data["author"]
    storerea_list = data["storerea"]
    publishingcompany_list = data["publishingcompany"]
    title_list = data["title"]

    @staticmethod
    def random_int():
        return random.randint(1, 1000)

    @classmethod
    def random_bookname(cls):
        return random.choice(cls.bookname_list)

    @classmethod
    def random_author(cls):
        return random.choice(cls.author_list)

    @classmethod
    def random_storerea(cls):
        return random.choice(cls.storerea_list)

    @classmethod
    def random_publishingcompany(cls):
        return random.choice(cls.publishingcompany_list)

    @classmethod
    def random_title(cls):
        return random.choice(cls.title_list)


fake.add_provider(Book_Info)
