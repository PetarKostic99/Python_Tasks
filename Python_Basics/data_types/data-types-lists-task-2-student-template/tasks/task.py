from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    fizzbuzz_list: ListType = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(i)
    return fizzbuzz_list


if __name__ == "__main__":
    assert get_fizzbuzz_list(15) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14,
                                     "FizzBuzz"]
    assert get_fizzbuzz_list(10) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
    assert get_fizzbuzz_list(3) == [1, 2, "Fizz"]
    assert get_fizzbuzz_list(5) == [1, 2, "Fizz", 4, "Buzz"]

