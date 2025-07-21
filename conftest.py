import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def collector_book():
    collector = BooksCollector()
    return collector