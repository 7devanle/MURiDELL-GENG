class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_of_nums = set(nums)
        max_sequence = 0
        
        for i in nums:
            if i - 1 not in set_of_nums:
                length = 1
                while i + length in set_of_nums:
                    length += 1
                max_sequence = max(length, max_sequence)
        return max_sequence