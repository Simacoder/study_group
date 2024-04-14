""" Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2."""

n = 50 
import sys
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length : {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)