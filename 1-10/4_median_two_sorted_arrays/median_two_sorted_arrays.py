class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []

        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    res.append(nums1[0])
                    nums1.pop(0)
                else:
                    res.append(nums2[0])
                    nums2.pop(0)
            elif not nums1:
                res.append(nums2[0])
                nums2.pop(0)
            else:
                res.append(nums1[0])
                nums1.pop(0)
            

        if len(res)%2 == 0:
            return float((res[len(res)/2] + res[len(res)/2-1]))/2
        else:
            return float(res[len(res)/2])