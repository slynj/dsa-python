class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        topFreq = []

        for i in range(len(nums) + 1):
            topFreq.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, val in count.items():
            topFreq[val].append(key)

        res = []

        for i in range(len(nums), -1, -1):
            for tf in topFreq[i]:
                res.append(tf)
                if len(res) == k:
                    return res

