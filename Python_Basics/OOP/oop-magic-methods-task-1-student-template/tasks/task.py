from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, other):
        if isinstance(other, str):
            result = []
            for value in self.values:
                result.append(f"{value} {other}")
            return result


counter_instance = Counter([1, 2, 3])
result_list = counter_instance + "Mississippi"
print(result_list)
