def longest_proper_prefix_suffix(P):
    length = len(P)
    longest_prefix_suffix = ""

    # Iterate from the length of the string down to 1 to find the longest match
    for i in range(length - 1, 0, -1):
        prefix = P[:i]
        suffix = P[-i:]
        if prefix == suffix:
            longest_prefix_suffix = prefix
            break
    
    return longest_prefix_suffix

# Test the function with the given string P
P = "cgtacgttcgtacg"
result = longest_proper_prefix_suffix(P)
print("Longest proper prefix that is also a suffix:", result)


"""
Initialization:

length stores the length of the string 
𝑃
P.
longest_prefix_suffix is initialized as an empty string to store the result.
Iterating Over Prefixes and Suffixes:

The loop starts from length - 1 (to ensure the prefix is proper, i.e., not equal to the whole string) and decrements down to 1.
For each iteration, it extracts the prefix P[:i] and the suffix P[-i:].
If the prefix matches the suffix, it updates longest_prefix_suffix and breaks out of the loop, since we are looking for the longest such prefix.
Returning the Result:

The function returns the longest proper prefix that is also a suffix.

"""