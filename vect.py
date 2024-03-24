# check vectors
from numpy import vectorize


class Vector:

     v = vectorize(5)
     v[1] = 23
     v[-1] = 45

     print(v[4])
     u = v + v
     print(u)

     total = 0

     for entry in v:
        total += entry