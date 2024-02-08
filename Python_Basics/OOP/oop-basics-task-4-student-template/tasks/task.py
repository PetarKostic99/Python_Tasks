class HistoryDict:
    def __init__(self, initial_dict):
        self.data = initial_dict
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)

    def get_history(self):
        return self.history[-5:]


# Example usage:
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())  # Output: ["bar"]

d.set_value("foo", 44)
print(d.get_history())  # Output: ["bar", "foo"]
