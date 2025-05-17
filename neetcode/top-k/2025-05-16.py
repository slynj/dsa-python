class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freqL = {}

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        for i in range(len(nums) + 1):
            freqL[i] = []
        
        for key, item in freq.items():
            freqL[item].append(key)

        res = []
        
        for i in range(len(nums), -1, -1):
            for elem in freqL[i]:
                res.append(elem)

                if len(res) == k:
                    return res
        
        

