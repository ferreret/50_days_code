"""
Coding Exercise: Monotonic Array

Question:

An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing.
An array is monotone decreasing if all  its elements from left to right are non-increasing. 
Given an integer array return true if the given array is monotonic, or false otherwise.
"""


def monotonic_array(array: list) -> bool:
    increase = True
    decrease = True

    for i in range(len(array) - 1):

        if array[i + 1] < array[i]:
            increase = False
        elif array[i + 1] > array[i]:
            decrease = False

        if not increase and not decrease:
            return False

    return increase or decrease


if __name__ == "__main__":
    print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # True
    print(monotonic_array([9, 8, 7, 6, 5, 4, 3, 2, 1]))  # True
    print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8, 1]))  # False
    print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8, 7]))  # False
    print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8, 8]))  # True
