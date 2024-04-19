"""
Coding Exercise: Sorted Squared Array

Question:
You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

Remember
You can solve this question in multiple ways.

Think about the following -

1.What would be the brute force way of solving this question ? What would be the Time and Space complexity of this approach?
2.Is there a better way to solve this with a more optimum Time complexity than the Brute force way ? 
"""

# BRUTE FORCE WAY
# def sorted_squared_array(arr):
#     arr = sorted([x**2 for x in arr])
#     return arr


# OPTIMAL WAY
def sorted_squared_array(arr):
    n = len(arr)
    result = [0] * n
    left = 0
    right = n - 1
    while left <= right:
        left_val = arr[left]
        right_val = arr[right]
        if abs(left_val) > abs(right_val):
            result[right - left] = left_val**2
            left += 1
        else:
            result[right - left] = right_val**2
            right -= 1
    return result


if __name__ == "__main__":
    print(sorted_squared_array([1, 2, 3, 5, 6, 8, 9]))
