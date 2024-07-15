class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        k = 1
        counter = 0

        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                counter += 1
                if counter == 1:
                    nums[k] = nums[i]
                    k += 1
            else:
                nums[k] = nums[i]
                k += 1
                counter = 0
            
        return k