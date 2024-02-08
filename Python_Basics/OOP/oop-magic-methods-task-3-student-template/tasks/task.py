from __future__ import annotations
from typing import Type


class Currency:
    def __init__(self, value):
        self.currency = None
        self.value = value

    def __str__(self):
        return f"{self.value} {self.currency}"

    @classmethod
    def course(cls, to_currency: Type[Currency]) -> str:
        return f"{cls.exchange_rate(to_currency)} {to_currency.currency} for 1 {cls.currency}"

    def to_currency(self, to_currency_cls: Type[Currency]):
        converted_value = self.value * self.exchange_rate(to_currency_cls)
        return to_currency_cls(converted_value)

    def __add__(self, other):
        target_currency_class = self.__class__
        converted_value = self.value + other.to_currency(self.__class__).value
        return target_currency_class(converted_value)

    def __lt__(self, other):
        self_converted = self.to_currency(self.__class__)
        other_converted = other.to_currency(self.__class__)
        return self_converted.value < other_converted.value

    def __le__(self, other):
        self_converted = self.to_currency(self.__class__)
        other_converted = other.to_currency(self.__class__)
        return self_converted.value <= other_converted.value

    def __eq__(self, other):
        self_converted = self.to_currency(self.__class__)
        other_converted = other.to_currency(self.__class__)
        return self_converted.value == other_converted.value

    def __gt__(self, other):
        self_converted = self.to_currency(self.__class__)
        other_converted = other.to_currency(self.__class__)
        return self_converted.value > other_converted.value

    def __ge__(self, other):
        self_converted = self.to_currency(self.__class__)
        other_converted = other.to_currency(self.__class__)
        return self_converted.value >= other_converted.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):
        return self.to_currency(other.__class__)(self.value - other.value)


class Euro(Currency):
    currency = "EUR"

    @staticmethod
    def exchange_rate(to_currency_cls):
        if to_currency_cls == Pound:
            return 100.0
        elif to_currency_cls == Dollar:
            return 2.0
        else:
            return 1.0


class Dollar(Currency):
    currency = "USD"

    @staticmethod
    def exchange_rate(to_currency_cls):
        if to_currency_cls == Pound:
            return 50.0
        elif to_currency_cls == Euro:
            return 0.5
        else:
            return 1.0


class Pound(Currency):
    currency = "GBP"

    @staticmethod
    def exchange_rate(to_currency_cls):
        if to_currency_cls == Euro:
            return 0.01
        elif to_currency_cls == Dollar:
            return 0.02
        else:
            return 1.0


# Test cases
e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
    f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
    f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
    f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
)

print(f"e = {e}")
print(f"r = {r}")
print(f"d = {d}\n")

print(
    f"e = {e}\n"
    f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
    f"e.to_currency(Pound)  = {e.to_currency(Pound)}\n"
    f"e.to_currency(Euro)    = {e.to_currency(Euro)}\n"
)

print(
    f"r = {r}\n"
    f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
    f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
    f"r.to_currency(Pound)  = {r.to_currency(Pound)}\n"
)

print(
    f"d = {d}\n"
    f"d.to_currency(Dollar) = {d.to_currency(Dollar)}\n"
    f"d.to_currency(Pound)  = {d.to_currency(Pound)}\n"
    f"d.to_currency(Euro)    = {d.to_currency(Euro)}\n"
)

print(f"e + r  =>  {e + r}")
print(f"r + d  =>  {r + d}")
print(f"d + e  =>  {d + e}")

# Other comparison methods
print(f"e > r  =>  {e > r}")
print(f"r > d  =>  {r > d}")
print(f"d > e  =>  {d > e}")
print(f"e > e =>   {e > e}")
print(f"d > d =>  {d > d}")
print(f"r > r =>  {r > r}")

print(f"e < r  =>  {e < r}")
print(f"r < d  =>  {r < d}")
print(f"d < e  =>  {d < e}")
print(f"e < e =>   {e < e}")
print(f"d < d =>   {d < d}")
print(f"r < r =>   {r < r}")

print(f"e == r =>  {e == r}")
print(f"r == d =>  {r == d}")
print(f"d == e =>  {d == e}")
print(f"e == e =>  {e == e}")
print(f"d == d =>  {d == d}")
print(f"r == r =>  {r == r}")
