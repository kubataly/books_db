from books_app import BooksApp
from DB.adapter import BooksDBAdapter
from DB.sqlite_adapter import SqliteBookDbAdapter

if __name__ == '__main__':
    adapter = SqliteBookDbAdapter("books.sqlite3")
    app = BooksApp(adapter)
    app.start()