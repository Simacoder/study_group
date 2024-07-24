# Maximum Odd Binary Number
"""
Problem Description
The problem is to find the maximum odd binary number that can be obtained by rearranging the bits of a given binary string.
Solution
To solve this, we can follow these steps:
1.	Count the number of '1's and '0's in the input binary string.
2.	Construct the maximum odd binary number:
o	To make the number odd, the least significant bit (rightmost bit) must be '1'.
o	Arrange the remaining '1's (total '1's count minus one) in the most significant positions to make the number as large as possible.
o	Fill the rest of the positions with '0's.
This strategy ensures the maximum possible odd binary number.


"""

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the number of '1's and '0's in the string
        count_ones = s.count('1')
        count_zeros = len(s) - count_ones
        
        # The maximum odd binary number can be formed by:
        # (count_ones - 1) '1's followed by all '0's and then one '1'
        if count_ones == 0:
            return ""
        
        max_odd_binary = '1' * (count_ones - 1) + '0' * count_zeros + '1'
        return max_odd_binary

# Example Usage
solution = Solution()
s = "0101"
print(solution.maximumOddBinaryNumber(s))  # Output: "1001"
