"""
Graph the functions 8n, 4nlog n, 2n2, n3, and 2n using a logarithmic scale
for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
point with x-coordinate at logn and y-coordinate at log y.
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

x = [10 **i for i in range(10)]

funct = [lambda x: 8*x,
         lambda x: 4*x*math.log(x),
         lambda x: 2*x**2,
         lambda x: x**3,
         ]

ys = []

for func in funct:
    ys.append(list(map(func, x)))

for y in ys:
    plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')

"""
The number of operations executed by algorithms A and B is 8nlog n and
2n2, respectively. Determine n0 such that A is better than B for n ≥ n0.

"""
x = [x/100 for x in range(1, 500)]
y1 = list(map(lambda x: 4*math.log(x), x))
y2 = x

plt.plot(x, y1)
plt.plot(x, y2)