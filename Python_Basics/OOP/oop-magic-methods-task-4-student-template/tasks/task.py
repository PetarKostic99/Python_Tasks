class PriceControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(f"{self.name.capitalize()} must be between 0 and 100.")
        instance.__dict__[self.name] = value


class NameControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if instance.__dict__.get(self.name) is not None:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")
        instance.__dict__[self.name] = value


class Book:
    price = PriceControl()
    author = NameControl()
    name = NameControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


# Example usage:
b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")

b.price = 55
print(b.price)

try:
    b.price = -12
except ValueError as e:
    print(e)

try:
    b.price = 101
except ValueError as e:
    print(e)

try:
    b.author = "new author"
except ValueError as e:
    print(e)

try:
    b.name = "new name"
except ValueError as e:
    print(e)
