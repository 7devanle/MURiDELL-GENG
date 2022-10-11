class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        longest = 0
        
        
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        sub = s[0]
        while r < len(s):
            if s[r] not in sub:
                sub += s[r]
                r += 1
            else:
                
                l, r = l + 1, l + 2
                sub = s[l]
            length = r - l
            longest = max(longest, length)
            
        return longest