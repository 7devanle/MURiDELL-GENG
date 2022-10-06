from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #Solution 1
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        sort_map = sorted(res.items(), key = lambda item: item[1], reverse = True)
        return [i[0] for i in sort_map[0:k]]
        
        #Solution 2 (From Neetcode)
        
#         count = {}
#         freq = [[] for i in range(len(nums)+1)]
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n,c in count.items():
#             freq[c].append(n)
#         res = []
#         for i in range(len(freq)-1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res