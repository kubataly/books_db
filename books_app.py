from DB.adapter import BooksDBAdapter
from models import Book

class BooksApp:
    def __init__(self, adapter: BooksDBAdapter):
        self.adapter = adapter

    def start(self):
        self.adapter.prepare()
        self._mainloop()

    def _mainloop(self):
        while True:
            command = input("\nВведите команду или напишите help:\n>> ")
            if command == "help":
                print("exit - Выйти")
                print("show all - Показать все книги")
                print("add - Добавить книгу")
                print("delete - Удалить книгу")
            elif command == "exit":
                print("Пока")
                break
            elif command == "show all":
                books = self.adapter.get_all_books()
                for book in books:
                    print(book)
            elif command == "add":
                name = input("Ок. Введите название книги")
                year = input("Введите год книги")
                author = input("Введите автора книги")
                book = Book(name, year, author, "Fiction")
                self.adapter.save_new_book(book)
                print("КНига успешно добавлена")
            elif command == "delete":
                id = input("Введите ID книги")
                book = self.adapter.get_book_by_id(id)
                if book is not None:
                    self.adapter.delete_book(id)
                else:
                    print("Книга не найдена")
            else:
                print(f"Команда '{command}' не найдена ")