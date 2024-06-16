def prefixes_that_are_suffixes(P):
    length = len(P)
    prefixes_suffixes = []

    for i in range(1, length + 1):
        prefix = P[:i]
        suffix = P[-i:]
        if prefix == suffix:
            prefixes_suffixes.append(prefix)
    
    return prefixes_suffixes

# Test the function with the given string P
P = "aaabbaaa"
result = prefixes_that_are_suffixes(P)
print("Prefixes of the string that are also suffixes:", result)

"""
Here is the step-by-step process to find these prefixes:

Identify Prefixes and Suffixes:

Prefixes are substrings that start at the beginning of 
𝑃
P.
Suffixes are substrings that end at the end of 
𝑃
P.
Match Prefixes and Suffixes:

Compare each prefix with the corresponding suffix of the same length.
Let's list and compare the prefixes and corresponding suffixes of 
𝑃
P:

Prefix of length 1: 
𝑃
[
0
:
1
]
=
"
𝑎
"
P[0:1]="a"

Corresponding suffix: 
𝑃
[
−
1
:
]
=
"
𝑎
"
P[−1:]="a"
Match: Yes
Prefix of length 2: 
𝑃
[
0
:
2
]
=
"
𝑎
𝑎
"
P[0:2]="aa"

Corresponding suffix: 
𝑃
[
−
2
:
]
=
"
𝑎
𝑎
"
P[−2:]="aa"
Match: Yes
Prefix of length 3: 
𝑃
[
0
:
3
]
=
"
𝑎
𝑎
𝑎
"
P[0:3]="aaa"

Corresponding suffix: 
𝑃
[
−
3
:
]
=
"
𝑎
𝑎
𝑎
"
P[−3:]="aaa"
Match: Yes
Prefix of length 4: 
𝑃
[
0
:
4
]
=
"
𝑎
𝑎
𝑎
𝑏
"
P[0:4]="aaab"

Corresponding suffix: 
𝑃
[
−
4
:
]
=
"
𝑏
𝑎
𝑎
𝑎
"
P[−4:]="baaa"
Match: No
Prefix of length 5: 
𝑃
[
0
:
5
]
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
"
P[0:5]="aaabb"

Corresponding suffix: 
𝑃
[
−
5
:
]
=
"
𝑏
𝑏
𝑎
𝑎
𝑎
"
P[−5:]="bbaaa"
Match: No
Prefix of length 6: 
𝑃
[
0
:
6
]
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
𝑎
"
P[0:6]="aaabba"

Corresponding suffix: 
𝑃
[
−
6
:
]
=
"
𝑎
𝑏
𝑏
𝑎
𝑎
𝑎
"
P[−6:]="abbaaa"
Match: No
Prefix of length 7: 
𝑃
[
0
:
7
]
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
𝑎
𝑎
"
P[0:7]="aaabbaa"

Corresponding suffix: 
𝑃
[
−
7
:
]
=
"
𝑎
𝑎
𝑏
𝑏
𝑎
𝑎
𝑎
"
P[−7:]="aabbaaa"
Match: No
Prefix of length 8: 
𝑃
[
0
:
8
]
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
𝑎
𝑎
𝑎
"
P[0:8]="aaabbaaa"

Corresponding suffix: 
𝑃
[
:
]
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
𝑎
𝑎
𝑎
"
P[:]="aaabbaaa"
Match: Yes
Thus, the prefixes of the string 
𝑃
=
"
𝑎
𝑎
𝑎
𝑏
𝑏
𝑎
𝑎
𝑎
"
P="aaabbaaa" that are also suffixes are:

"a"
"aa"
"aaa"
"aaabbaaa"
"""
