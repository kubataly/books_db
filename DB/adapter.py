from models import Book

class BooksDBAdapter():
    def __init__(self):
        self.books = []

    def prepare(self):
        pass

    def get_all_books(self) -> list:
        return []

    def save_new_book(self, book: Book):
        pass

    def get_book_by_id(self, id):
        pass

    def delete_book(self, id):
        pass

    def update_book(self, book):
        pass
