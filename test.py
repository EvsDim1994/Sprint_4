import pytest


class TestBooksCollector():

    
    @pytest.mark.parametrize('name', 
        [
        'Я',
        'Очень длинное название книги, которое 40',
        ]
    )
    def test_add_new_book_with_40_symbols_and_1_symblos(self, collector_book, name):
        collector_book.add_new_book(name)
        assert len(collector_book.get_books_genre()) == 1

    @pytest.mark.parametrize('name', 
        [
        "",
        'Очень длинное название книги, которое содержит больше 41 символа',
        ]
    )
    def test_add_new_book_with_lenght_more_than_41_symbols_and_null(self, collector_book, name):
        collector_book.add_new_book(name)
        assert not collector_book.get_book_genre(name)

    def test_add_new_book_without_genre(self, collector_book):
        collector_book.add_new_book('Война и мир')
        assert collector_book.get_book_genre('Война и мир') == ''

    @pytest.mark.parametrize('name, genre', 
        [
            ['оно', 'Ужасы'],
            ['Звездные войны', 'Фантастика'],
            ['Пуаро', 'Детективы'],
            ['pinocchio', 'Мультфильмы'],
            ['Фантомас', 'Комедии']
        ]
    )
    def test_set_book_genre_for_new_book(self, collector_book, name, genre):
        collector_book.add_new_book(name)
        collector_book.set_book_genre(name, genre)
        assert collector_book.get_book_genre(name) == genre

    def test_add_new_book_with_the_same_name(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        collector_book.add_new_book('Оно')
        assert len(collector_book.get_books_genre()) == 1

    def test_get_books_with_specific_genre_get_detective(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        collector_book.add_new_book('Пуаро')
        collector_book.set_book_genre('Пуаро', 'Детективы')
        assert collector_book.get_books_with_specific_genre('Детективы')[0] == 'Пуаро'

    def test_get_books_for_children_get_pinocchio(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        collector_book.add_new_book('Пуаро')
        collector_book.set_book_genre('Пуаро', 'Детективы')
        collector_book.add_new_book('pinocchio')
        collector_book.set_book_genre('pinocchio', 'Мультфильмы')
        assert collector_book.get_books_for_children()[0] == 'pinocchio' and len(collector_book.get_books_for_children()) == 1

    def test_add_book_in_favorites_for_new_book(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        collector_book.add_book_in_favorites('Оно')
        assert 'Оно' in collector_book.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_for_with_2_books(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.add_new_book('Пуаро')
        collector_book.add_book_in_favorites('Оно')
        collector_book.add_book_in_favorites('Пуаро')
        assert len(collector_book.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_for_added_book(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        collector_book.add_book_in_favorites('Оно')
        collector_book.delete_book_from_favorites('Оно')
        assert not collector_book.get_list_of_favorites_books()

    def test_get_books_genre_for_2_books(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.add_new_book('Пуаро')
        assert len(collector_book.get_books_genre()) == 2

    def test_get_books_genre_with_book_genre(self, collector_book):
        collector_book.add_new_book('Оно')
        collector_book.set_book_genre('Оно', 'Ужасы')
        assert collector_book.get_books_genre().get('Оно') == 'Ужасы'



    