# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst_h = {}
        lst = [[] for i in range(len(nums) + 1)]

        for n in nums:
            lst_h[n] = 1 + lst_h.get(n, 0)
        
        for key, val in lst_h.items():
            lst[val].append(key)
        
        topk = []

        for i in range(len(lst) - 1, 0, -1):
            for l in lst[i]:
                topk.append(l)
                if (len(topk) == k): return topk
        

        
