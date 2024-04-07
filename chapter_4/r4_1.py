# eexrecise 1


"""
Describe a recursive algorithm for finding the maximum element in a sequence,
S, of n elements. What is your running time and space usage?

"""

def rec_find_max(S, index):
    if index == len(S)-1:
        return S[index]
    return max(S[index], rec_find_max(S, index + 1))

def find_max(S):
    return rec_find_max(S, 0)

print(find_max([1, 2,4,5, 8]))

"""
running time is O(n), as N calls recursion , eac taking O(1) time.
"""
