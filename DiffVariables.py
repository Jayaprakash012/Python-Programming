class LibraryBook:
    book_name = ""   # public variable

    def __init__(self, name, price):
        self.book_name = name
        self.__book_price = price   # private variable

    def set_price(self, price):
        self.__book_price = price

    def get_price(self):
        return self.__book_price


class DigitalBook(LibraryBook):
    def update_price(self, new_price):
        self.set_price(new_price)


b = DigitalBook("Python", 500)

print("Book Name:", b.book_name)
print("Original Price:", b.get_price())

b.update_price(600)

print("Updated Price:", b.get_price())