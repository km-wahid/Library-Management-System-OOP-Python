class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def view_book_info(cls):
        if not cls.book_list:
            return "No books available."
        return "\n".join(
            [f"ID: {book.get_book_id()}, Title: {book.get_title()}, Author: {book.get_author()}, Available: {book.get_availability()}"
             for book in cls.book_list]
        )

    @classmethod
    def borrow_book(cls, book_id):
        for book in cls.book_list:
            if book.get_book_id() == book_id:
                if book.get_availability():
                    book.set_availability(False)
                    return f"You have successfully borrowed the book: {book.get_title()}"
                else:
                    return f"Sorry, the book '{book.get_title()}' is currently not available."
        return "Book ID not found."

    @classmethod
    def return_book(cls, book_id):
        for book in cls.book_list:
            if book.get_book_id() == book_id:
                if not book.get_availability():
                    book.set_availability(True)
                    return f"Thank you for returning the book: {book.get_title()}"
                else:
                    return f"The book '{book.get_title()}' was not borrowed."
        return "Book ID not found."


class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = bool(availability)

    # Getter methods for private attributes
    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_availability(self):
        return self.__availability

   
    def set_availability(self, availability): # setter
        self.__availability = availability

    def show_details(self):
        return (f"Book id is: {self.get_book_id()}",
                f"Title is: {self.get_title()}",
                f"Author name is: {self.get_author()}",
                f"Is it available: {self.get_availability()}")


book1 = Book(101, "Alchemist", "Paulo Coelho", True)
book2 = Book(102, "Spy", "Paulo Coelho", True)
book3 = Book(103, "Atomic Habits", "James Clear", True)
book4 = Book(104, "How to Talk", "Dobelli", True)

Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)


while True:
    print(" --------Welcome to Library-------- " )
    print("1. View all books")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")

    user = input("Please enter your choice (1-4): ")

    if user == "1":
        print("\nAvailable Books:")
        print(Library.view_book_info())
    elif user == "2":
        try:
            book_id = int(input("Enter the Book ID to borrow: "))
            print(Library.borrow_book(book_id))
        except ValueError:
            print("Invalid Book ID. Please enter a numeric value.")
    elif user == "3":
        try:
            book_id = int(input("Enter the Book ID to return: "))
            print(Library.return_book(book_id))
        except ValueError:
            print("Invalid Book ID. Please enter a numeric value.")
    elif user == "4":
        print("Exiting the program!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
