class Field:
    __value = None

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value


if __name__ == "__main__":
    obj = Field()
    assert obj.get_value() is None

    obj.set_value(100)
    assert obj.get_value() == 100
