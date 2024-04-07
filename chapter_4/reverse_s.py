# reverse with linear recurive

def reverse(S, start, stop):
    """ Reverse elements in implict slice S[Start: stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop -1], S[start]
        reverse(S, start + 1, stop -1)