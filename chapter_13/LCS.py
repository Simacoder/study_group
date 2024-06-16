def LCS(X, Y):
    """ Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]. """
    n, m = len(X), len(Y)
    L = [[0] (m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = L[j][k] + 1
            else:
              L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L

""" 
The running time of the algorithm of the LCS algorithm is easy to analyze,
for it is dominated by two nested for loops, with the outer one iterating n times
and the inner one iterating m times. Since the if-statement and assignment inside
the loop each requires O(1) primitive operations, this algorithm runs in O(nm)
time. Thus, the dynamic programming technique can be applied to the longest
common subsequence problem to improve significantly over the exponential-time
brute-force solution to the LCS problem.

"""