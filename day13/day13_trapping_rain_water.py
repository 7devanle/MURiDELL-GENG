class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_left = height[0]
        max_right = height[len(height) - 1]
        total_area = 0
        while l < r:
            if max_left < max_right:
                total_area += max_left - height[l]
                l += 1
            else:
                total_area += max_right - height[r]
                r -= 1
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
        return total_area