# summation function with recursive call

S = [1 , 4, 3, 8]
def linear_sum(S, n):
    """ return the sum of the first n numbers of sequences S"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]
    

print(linear_sum(S, 3))