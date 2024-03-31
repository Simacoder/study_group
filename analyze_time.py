from time import time 
start_time = time()
# Run the algorithm 
def find_max(data):
    """" Returning the maximum element from the nonempty list"""
    data = [1, 4, 3, 2, 9, 7]
    #data.sort()
    biggest= data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
df = []
print("the highest number is the list is: ", find_max(df))
end_time = time()

elapsed = end_time - start_time
print("The run time is: ", elapsed)
