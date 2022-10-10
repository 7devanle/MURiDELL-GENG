class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)
            print(maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea