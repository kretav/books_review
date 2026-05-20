import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except json.JSONDecodeError:
        return []


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(book):
    books = load_books()

    for existing in books:
        if (
            existing["author"].lower() == book["author"].lower()
            and existing["title"].lower() == book["title"].lower()
        ):
            print("Такая книга уже существует.")
            return

    books.append(book)
    save_books(books)


def delete_book(title):
    books = load_books()

    updated_books = [
        book for book in books
        if book["title"].lower() != title.lower()
    ]

    save_books(updated_books)