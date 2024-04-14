# Dynamic Array in python 
import sys 
data = []
for k in range(0):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size of Bytes: {1:4d}'.format(a, b))
    data.append(None)