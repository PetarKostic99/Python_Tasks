from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    try:
        a, b = map(int, str_with_ints.split())
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error code: division by zero"
    except ValueError as e:
        return f"Error code: {str(e)}"


print(divide("0 2"))
print(divide("4 0"))
print(divide("* 1"))
