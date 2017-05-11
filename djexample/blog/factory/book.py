# -*- coding: utf-8 -*-

from djexample.fake_factory import factory

from blog.models import Book


class BookFactory(factory.DjangoModelFactory):
    """Book factory"""

    name = factory.Faker('word')
    extra_data = factory.Faker('random_string_dict')

    class Meta:
        model = Book

    @staticmethod
    def create_book(amount=1, **kwargs):
        return BookFactory.create_batch(amount, **kwargs)
