class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def fly(self):
        return f"{self.name} bird can fly"

    def __str__(self):
        return f"{self.name} bird"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return "It eats mostly fish"

    def fly(self):
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name, ration)

    def __str__(self):
        abilities = ", ".join(["walk", "swim and fly"])
        return f"{self.name} bird can {abilities}"

    #Override the eat method to use the NonFlyingBird's eat method
    def eat(self):
        return NonFlyingBird.eat(self)


# Examples
b = Bird("Any")
print(b.walk())

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
try:
    print(p.fly())
except AttributeError as e:
    print(repr(e))
print(p.eat())

c = FlyingBird("Canary")
print(str(c))
print(c.eat())

s = SuperBird("Gull")
print(str(s))
print(s.eat())
