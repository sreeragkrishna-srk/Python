from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class LibraryItem(ABC):
    def __init__(self, title: str, item_id: str):
        self.title = title
        self.__item_id = item_id  # Private attribute

    def get_item_id(self) -> str:
        return self.__item_id

    @abstractmethod
    def calculate_late_fee(self, days_overdue: int) -> float:
        pass


# Inheritance and Polymorphism
class Book(LibraryItem):
    def __init__(self, title: str, item_id: str, author: str):
        super().__init__(title, item_id)
        self.author = author

    def calculate_late_fee(self, days_overdue: int) -> float:
        fee = days_overdue * 0.50
        print(f"Late fee for Book '{self.title}': ${fee:.2f}")
        return fee


class MediaDVD(LibraryItem):
    def __init__(self, title: str, item_id: str, runtime_mins: int):
        super().__init__(title, item_id)
        self.runtime_mins = runtime_mins

    def calculate_late_fee(self, days_overdue: int) -> float:
        fee = days_overdue * 2.00
        print(f"Late fee for DVD '{self.title}': ${fee:.2f}")
        return fee


# Execution
book_item = Book("Python Crash Course", "BK-101", "Eric Matthes")
book_item.calculate_late_fee(4)

dvd_item = MediaDVD("Python Essentials Video", "DVD-909", 120)
dvd_item.calculate_late_fee(4)