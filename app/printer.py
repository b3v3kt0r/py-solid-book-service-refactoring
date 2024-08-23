from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_book(self, book) -> None:
        pass


class PrinterConsole(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrinterReverse(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
