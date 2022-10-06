import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)

        #Solution 1
        for s in strs:
            sorted_s = sorted(s)
            res[tuple(sorted_s)].append(s)
        return res.values()
        
        #Solution 2 (From Neetcode)
#         for s in strs:
#             count = [0] * 26 #a...z
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             res[tuple(count)].append(s)
#         return res.values()