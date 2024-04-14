""" Execute the experiment from Code Fragment 5.1 and compare the results
on your system to those we report in Code Fragment 5.2.
"""

import sys

def func1(n):
    data = []
    b_old = sys.getsizeof(data)
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f'Length: {a: 3d}; size in bytes: {b:4d}', end = '')
        if b_old != b:
            print('\\t A jump of: {0} bytes, or a ratio of {1}'.format((b-b_old), (b/b_old)))
        else:
            print('')
        data.append(None)
        b_old = b

func1(100)
