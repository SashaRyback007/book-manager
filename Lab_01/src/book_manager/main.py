from book_manager.models import Book
from book_manager.services import (
    add_book,
    calculate_average_pages,
    filter_by_year,
    find_books_by_author,
    find_largest_book,
)


def create_demo_books() -> list[Book]:
    return [
        Book(
            title="The Hobbit",
            author="J.R.R. Tolkien",
            year=1937,
            pages=310,
        ),
        Book(
            title="1984",
            author="George Orwell",
            year=1949,
            pages=328,
        ),
        Book(
            title="Animal Farm",
            author="George Orwell",
            year=1945,
            pages=112,
        ),
        Book(
            title="The Lord of the Rings",
            author="J.R.R. Tolkien",
            year=1954,
            pages=1178,
        ),
        Book(
            title="Brave New World",
            author="Aldous Huxley",
            year=1932,
            pages=288,
        ),
    ]


def print_books(books: list[Book]) -> None:
    if not books:
        print("No books found.")
        return

    print(f"{'Title':<25} {'Author':<20} {'Year':<6} {'Pages':<6}")
    print("-" * 60)
    for book in books:
        print(
            f"{book.title:<25} "
            f"{book.author:<20} "
            f"{book.year:<6} "
            f"{book.pages:<6}"
        )


def main() -> None:
    books = create_demo_books()

    print("All Books in Library:")
    print_books(books)

    new_book = Book(
        title="Fahrenheit 451",
        author="Ray Bradbury",
        year=1953,
        pages=256,
    )
    add_book(books, new_book)
    print(f"\nAdded new book: {new_book.short_info}")

    search_author = "Orwell"
    print(f"\nBooks by '{search_author}':")
    author_books = find_books_by_author(books, search_author)
    print_books(author_books)

    target_year = 1937
    print(f"\nBooks published in {target_year}:")
    year_books = filter_by_year(books, target_year)
    print_books(year_books)

    largest = find_largest_book(books)
    if largest:
        print(f"\nLargest book: {largest.short_info} with {largest.pages} pages")

    avg_pages = calculate_average_pages(books)
    print(f"Average pages across all books: {avg_pages:.1f}")


if __name__ == "__main__":
    main()