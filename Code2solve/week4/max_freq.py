nums =[1, 2, 2, 3, 3, 3]
class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store frequency of each number
        freq_dict = {}
        max_freq = 0
        total_max_freq = 0

        # Single pass through the array
        for num in nums:
            # Update frequency
            freq_dict[num] = freq_dict.get(num, 0) + 1
            current_freq = freq_dict[num]

            # Update max_freq and total_max_freq
            if current_freq > max_freq:
                max_freq = current_freq
                total_max_freq = current_freq
            elif current_freq == max_freq:
                total_max_freq += current_freq

        return total_max_freq
