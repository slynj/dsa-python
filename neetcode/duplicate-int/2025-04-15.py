class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}

        for n in nums:
            numbers[n] = numbers.get(n, 0) + 1

        return len(numbers.keys()) != len(nums)

        
