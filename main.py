from models import Book
from storage import load_books, add_book, delete_book
from stats import average_rating, author_statistics


def show_books():
    books = load_books()

    if not books:
        print("Список книг пуст.")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. {book['author']} - "
            f"{book['title']} | "
            f"Оценка: {book['rating']} | "
            f"Дата: {book['read_date']}"
        )


def main():
    while True:
        print("\n=== Трекер книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            author = input("Автор: ")
            title = input("Название: ")
            rating = int(input("Оценка (1-5): "))
            read_date = input("Дата прочтения: ")

            book = Book(author, title, rating, read_date)

            add_book(book.to_dict())

        elif choice == "2":
            show_books()

        elif choice == "3":
            books = load_books()
            avg = average_rating(books)

            print(f"Средняя оценка: {avg:.2f}")

        elif choice == "4":
            books = load_books()
            stats = author_statistics(books)

            for author, count in stats.items():
                print(f"{author}: {count} книг")

        elif choice == "5":
            title = input("Введите название книги: ")
            delete_book(title)

        elif choice == "6":
            print("Выход...")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()