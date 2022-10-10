class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        alpha_start = ord("a")
        alpha_end = ord("z")
        num_start = ord("0")
        num_end = ord("9")
        s_list = []
        for i in s:
            if self.isAlphaNumeric(i):
                s_list.append(i)
        print(s_list)
        print(s_list[::-1])
        return s_list == s_list[::-1]

        # Two pointer solution
        # l, r = 0, len(s)-1
        # while l < r:
        #     while l < r and not self.isAlphaNumeric(s[l]):
        #         l += 1
        #     while r > l and not self.isAlphaNumeric(s[r]):
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True
    
    def isAlphaNumeric(self, c):
        return (ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9") or
                ord("A") <= ord(c) <= ord("Z") )