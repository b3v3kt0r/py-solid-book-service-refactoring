from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self, book) -> None:
        pass


class DisplayConsole(Display):
    def display(self, book) -> None:
        print(book.content)


class DisplayReverse(Display):
    def display(self, book) -> None:
        print(book.content[::-1])
