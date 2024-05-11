# binary search algorithm 

data =[2, 4, 6, 8, 9, 10, 12]
target = 8
low = 0
high = len(data)- 1

def binary_search(data, target, low, high):
    """ return true if the target is found """
    if low > high:
        return False
    else:
        mid = (low + high)// 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the left side
            return binary_search(data, target, low, mid - 1)
        
        else:
            # recur on the right side
            return binary_search(data, target, mid + 1, high)

print(binary_search(data, target, low, high))
        
        