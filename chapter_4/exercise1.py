# exercise 1

"""
Describe a recursive algorithm for finding the maximum element in a sequence,
S, of n elements. What is your running time and space usage?
"""

def rec_find_max(S, index):
    if index == len(S)- 1:
        return S[index]
    return max(S[index], rec_find_max(S, index + 1))

def find_max(S):
    return rec_find_max(S, 0)

print(find_max([1, 3, 5, 7, 9, 13, 15]))
print(find_max([1, 3, 45, 5, 7, 9, 8]))
print(find_max([15, 13, 11, 9, 7, 5, 3, 1]))

"""
 Running time is O(n) linear time as N calls to recursion one (O(1))
 the Space is also O(n) since recursion trace calls for activation record at one 
"""
