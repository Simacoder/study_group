from time import time 

start_time = time()
# run algorithm 
def find_max():
    """ Returning the maximum from nonempty Python list"""

    data = [1, 4, 6, 2, 9, 7]
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
    

print(find_max())
end_time = time()
elapsed = end_time - start_time
print(elapsed)