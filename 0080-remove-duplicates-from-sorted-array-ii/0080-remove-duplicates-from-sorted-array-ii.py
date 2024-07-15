class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        k = 2

        for i in range(2, length):
            # 새로운 숫자면, 바꿔줬으니까 2번째로 같게온게 k - 2
            # 새로운 숫자라는게 i - 1 비교, 2번째로 같을수도 있으니까 k - 2
            if nums[i - 1] != nums[i] or nums[k - 2] != nums[i]:
                nums[k] = nums[i]
                k += 1
        # k = 1
        # counter = 0

        # for i in range(1, length):
        #     if nums[i] == nums[i - 1]:
        #         counter += 1
        #         if counter == 1:
        #             nums[k] = nums[i]
        #             k += 1
        #     else:
        #         nums[k] = nums[i]
        #         k += 1
        #         counter = 0
            
        return k