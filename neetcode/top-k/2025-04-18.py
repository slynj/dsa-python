class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        countList = []
        res = []

        for i in range(len(nums) + 1):
            countList.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, val in count.items():
            countList[val].append(key)
        
        for i in range(len(nums), -1, -1):
            for li in countList[i]:
                res.append(li)
                if len(res) == k:
                    return res
        
        

