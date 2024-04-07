# exercise 2 with recurive call

"""
Draw the recursion trace for the computation of power(2,5), using the
traditional function implemented in Code Fragment 4.11.
"""

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
"""
For this implemention (x = 2, n = 5) , the   recursion trace is:
power(2, 5) return 16*2 = 32
    power(2, 4) return 8*2 = 16
        power (2, 3) returns 6 * 2 = 12
            power (2, 2) RETURN 2 * 2 = 4
                power(2,1) returns 2*1 = 2
                    power(2, 0) returns 1

"""

print(power(2, 5))