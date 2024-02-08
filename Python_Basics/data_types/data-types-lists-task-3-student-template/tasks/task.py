from typing import List


def foo(nums: List[int]) -> List[int]:
    if not nums:
        return []

        # Calculate the product of all elements to the left of each index
    left_products = [1] * len(nums)
    left_product = 1
    for i in range(1, len(nums)):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Calculate the product of all elements to the right of each index and multiply with the left product
    right_product = 1
    for i in range(len(nums) - 2, -1, -1):
        right_product *= nums[i + 1]
        left_products[i] *= right_product

    return left_products


if __name__ == "__main__":
    assert foo([2, 5, 4, 3]) == [60, 24, 30, 40]
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
    assert foo([]) == []
