class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i1 = m - 1
        i2 = n - 1
        i = m + n - 1

        while i2 >= 0:
            # i1 0보다 작을때면 무조건 nums2가 들어갈테니까
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -=1

        # index1 = m - 1 #if m != 0 else m
        # index2 = n - 1 #if n != 0 else n
        # current = m + n - 1
        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        # else:
        #     for i in range(m + n):
                
        #         if index2 < 0:
        #             break
        #         if index1 < 0:
        #             if current == 0:
        #                 nums1[current] = nums2[index2]
        #                 break

        #             nums1[current] = nums2[index2]
        #             index2 -= 1
        #         else:
        #             if nums1[index1] >= nums2[index2]:
        #                 nums1[current] = nums1[index1]
        #                 index1 -= 1
        #             else:
        #                 nums1[current] = nums2[index2]
        #                 index2 -= 1
        #         current -= 1

                
                
