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