def find_max():
    """ Returning the maximum from nonempty Python list"""

    data = [1, 4, 6, 2, 9, 7]
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
    

print(find_max())