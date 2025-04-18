class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashN = {}

        for n in nums:
            hashN[n] = 1 + hashN.get(n, 0)
        
        hashN = sorted(hashN.items(), key=lambda item: item[1], reverse=True)
        hashN = list(dict(hashN).keys())

        return hashN[:k]
        # this is O(n + n log n) -> O(n log n) time complexity

