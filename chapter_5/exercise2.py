""" In Code Fragment 5.1, we perform an experiment to compare the length of
a Python list to its underlying memory usage. Determining the sequence
of array sizes requires a manual inspection of the output of that program.
Redesign the experiment so that the program outputs only those values of
k at which the existing capacity is exhausted. For example, on a system
consistent with the results of Code Fragment 5.2, your program should
output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . ."""

import sys 

def array_jump(n):
    data = []
    size_old = 0
    for _ in range(n):
        size = sys.getsizeof(data)
        if size != size_old:
            print(len(data), end = ',')
        size_old = size
        data.append(None)

array_jump(26)