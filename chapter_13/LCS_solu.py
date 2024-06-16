def LCS_solution(X, Y, L):
    """ Return the longest common substring of X and Y, given LCS table L. """
    solution = [ ]
    j,k = len(X), len(Y)
    while L[j][k] > 0:
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
          k -= 1
    return ''.join(reversed(solution))

""" 
Illustration of the algorithm for constructing a longest common subsequence
from the array L. A diagonal step on the highlighted path represents the use
of a common character (with that character’s respective indices in the sequences
highlighted in the margins).
"""
                                        