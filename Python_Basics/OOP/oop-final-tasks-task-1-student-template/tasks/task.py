class Sun:
    _instance = None

    def __init__(self):
        raise ValueError("Use Sun.inst() to get an instance, do not instantiate directly.")

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = super(Sun, cls).__new__(cls)
            # Initialization logic can go here
        return cls._instance


# Example usage:
p = Sun.inst()
f = Sun.inst()

print(p is f)  # Output: True
