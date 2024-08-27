class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(m+n == 1 and n == 1):
            nums1[0] = nums2[0]

        else:
            count = 0
            while count < n:
                nums1[m+count] = nums2[count]
                count += 1
            nums1.sort()

        return nums1