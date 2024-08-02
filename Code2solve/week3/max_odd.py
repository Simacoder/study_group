class Solution(object):
    def maximumOddBinaryNumber(self, s):
        # Count the number of '1' and '0' 
        count_ones = s.count('1')
        count_zeros = len(s) - count_ones

        if count_ones == 0:
            return ""
        
        max_odd_binary = '1' * (count_ones - 1) + '0' * count_zeros + '1'
        return max_odd_binary
    

solution =  Solution()
s = "0101"
print(solution.maximumOddBinaryNumber(s))