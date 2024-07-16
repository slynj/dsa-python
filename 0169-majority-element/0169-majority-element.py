class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        n = ceil(length / 2)

        if length == 1 or length == 2:
            return nums[0]

        if nums[0] == nums[n - 1] and (n - 1 < length):
            return nums[0]
        for i in range(1, length):
            if nums[i - 1] != nums[i]:

                if nums[i] == nums[i + n - 1] and (i + n - 1 < length):
                
                    return nums[i]

        # for num in nums:
        #     counter = 0
        #     for num2 in nums:
        #         if num == num2:
        #             counter += 1
        #         if counter >= n:
        #             return num

