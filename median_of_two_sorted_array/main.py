class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        concat_array = nums1 + nums2 
        concat_array.sort()          

        n = len(concat_array)
        if n % 2 == 0:
            return (concat_array[n // 2] + concat_array[(n // 2) - 1]) / 2.0
        else:
            return concat_array[n // 2]


nums1, nums2 = [1, 3], [2]
nums1, nums2 = [1, 2], [3, 4]
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
