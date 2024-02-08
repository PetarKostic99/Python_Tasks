from typing import List


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    # Initialize an empty list to store the multiplication table
    table = []

    for i in range(row_start, row_end + 1):
        row = []
        for j in range(column_start, column_end + 1):
            # Calculate the product and append it to the row
            row.append(i * j)
        # Append the row to the table
        table.append(row)

    return table


if __name__ == "__main__":
    assert check(2, 4, 3, 7) == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
    assert check(1, 5, 1, 5) == [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20],
                                 [5, 10, 15, 20, 25]]
    assert check(0, 0, 0, 0) == [[0]]
