"""
Explanation:
Initialization: first_max and second_max are initialized to negative infinity to handle the smallest possible values in the list.
Traversal and Update:
If the current element is greater than first_max, it means we've found a new maximum. Therefore, the current first_max becomes the second_max, and the new element becomes first_max.
If the current element is not greater than first_max but is greater than second_max and not equal to first_max, then update second_max.
Edge Cases:
If the list has less than two elements, there can't be a second maximum.
If all elements in the list are the same, there is no distinct second maximum.
This solution is efficient with a time complexity of 
𝑂(𝑛)
O(n), where 𝑛 is the number of elements in the list, as it requires a single pass through the list.

"""
# walktrough 
"""
Example Walkthrough:
Consider the list: [3, 5, 2, 5, 1]

Initialize:

first_max = -∞
second_max = -∞
First element (3):

3 > first_max (True)
Update:
second_max = first_max = -∞
first_max = 3
Second element (5):

5 > first_max (True)
Update:
second_max = first_max = 3
first_max = 5
Third element (2):

2 > first_max (False)
2 > second_max (True)
Update:
second_max = 2
Fourth element (5):

5 > first_max (False)
5 != first_max (False, because 5 == 5)
No update
Fifth element (1):

1 > first_max (False)
1 > second_max (False)
No update
Final values:

first_max = 5
second_max = 3
Thus, the second maximum number in the list is 3.

This flowchart and example should help in understanding how the algorithm works step by step.








"""

def find_second_maximum(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find the second maximum

    first_max = second_max = float('-inf')

    for number in arr:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max and number != first_max:
            second_max = number

    if second_max == float('-inf'):
        return None  # No second maximum found
    return second_max

# Example usage
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_second_maximum(arr)
    if result is None:
        print("No second maximum number found")
    else:
        print(result)
