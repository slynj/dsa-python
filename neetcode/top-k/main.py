# https://neetcode.io/problems/top-k-elements-in-list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst_h = {}
        sort = {}

        for n in nums:
            lst_h[n] = 1 + lst_h.get(n, 0)
        
        sort = sorted(lst_h, key=lst_h.get, reverse = True)
        
        return sort[:k]
        