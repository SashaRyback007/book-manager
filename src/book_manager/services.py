from book_manager.models import Book


def add_book(books: list[Book], book: Book) -> None:
    books.append(book)


def find_books_by_author(books: list[Book], author: str) -> list[Book]:
    normalized_author = author.strip().casefold()
    return [
        book for book in books
        if normalized_author in book.author.casefold()
    ]


def filter_by_year(books: list[Book], year: int) -> list[Book]:
    return [book for book in books if book.year == year]


def find_largest_book(books: list[Book]) -> Book | None:
    if not books:
        return None
    return max(books, key=lambda book: book.pages)


def calculate_average_pages(books: list[Book]) -> float:
    if not books:
        return 0.0
    total_pages = sum(book.pages for book in books)
    return total_pages / len(books)