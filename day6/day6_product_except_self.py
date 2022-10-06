class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)
        prev = 1
        for i in range(len(nums)):
            output[i] = prev
            prev *= nums[i]
        print(output)
        after = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= after
            after *= nums[i]
        return output