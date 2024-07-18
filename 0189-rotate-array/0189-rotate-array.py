class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        # length = len(nums)
        
        # # print(nums[k + 1:] + nums[:k + 1])
        # k += 0 if k % 2 == 0 else 1

        # print(nums[k:])
        # print(nums[:k])

        # new = nums[k:] + nums[:k]


        # new1 = nums
        # new2 = nums
        # print(new1)
        # print(new2)
        # print(new1[k:])
        # print(new2[:k])
        # new = (new1[k:] + new2[:k])
        # # new=[x for n in (new1,new2) for x in n]
        # # new = nums[k:].extend(nums[:k])
        # # # print(new)
        # # # # nums = new
        # print(new)
        # # print(new[0])

        # for i in range(length):
        #     print(new[i])
        #     nums[i] = new[i]
        #     print(nums[i])

        # # i = 0
        # current = 0
        # while True:
        #     index = i + k if i + k < length else i + k - length
        #     print(nums[i])
        #     print(nums[index])
        #     temp = nums[index]
        #     nums[index] = nums[i]

        #     print([1, 2, 3] + [2, 4])
            
        #     index = index + k if index + k < length else index + k - length
        #     nums[index] = temp
        #     print("index:", index)
        #     if index == k - 1:
        #         break

        #     i += 1

            
        