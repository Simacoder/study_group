# tail recursive call of binary search 
data = [1, 3, 5, 7, 9, 11, 13, 15]

def binary_search_iter(data, target):
    """Return True if target is found in the given python list"""
    low = 0
    high = len(data)-1
    while low <= high:
        mid = (low + high)// 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else: 
            low = mid + 1
    return False

print(binary_search_iter(data, target= 13))