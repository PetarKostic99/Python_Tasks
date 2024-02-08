class Counter:
    def __init__(self, start=0, stop=None):
        self.value = start
        self.stop = stop

    def increment(self):
        if self.stop is not None and self.value == self.stop:
            print("The maximal value is reached.")
        else:
            self.value += 1

    def get(self):
        return self.value


# Case 1
c1 = Counter(start=42)
c1.increment()
print(c1.get())

# Case 2
c2 = Counter()
c2.increment()
print(c2.get())
c2.increment()
print(c2.get())

# Case 3
c3 = Counter(start=42, stop=43)
c3.increment()
print(c3.get())
c3.increment()
print(c3.get())
