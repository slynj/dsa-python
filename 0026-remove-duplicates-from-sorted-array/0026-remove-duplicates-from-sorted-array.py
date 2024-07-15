class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0: return 0
        if length == 1: return 1
        
        k = 1 
        for i in range(1, length): 
            if nums[i] != nums[i-1]: 
                nums[k] = nums[i]
                k += 1
        return k

        # k = 0
        # for i in range(length):
        #     if i < length - 2 and nums[i] == nums[i + 1]:
        #         continue
        #     nums[k] = nums[i]
        #     k += 1
        # return k
        # # index = 0
        # # end_index = length
        # # k = length
        # p1 = 0
        # p2 = 1
        
        # while p1 < length:
        #     if (nums[p1] == nums[p2]):
        #         nums = nums[:]
        #     else:
        #         p1 += 1
        #         p2 += 1
        #     # print(k)
        #     # print(nums)
        #     # print(index)
        #     # if nums[index] == nums[index + 1]:
                
        #     #     for i in range(index, end_index - index - 1):
        #     #         nums[i] = nums[i + 1]
                    
        #     #     k -= 1
        #     #     end_index -= 1
        #     # if nums[index] != nums[index + 1]: 
        #     #     index += 1
        # print(k)
        # return k
        