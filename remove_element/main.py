class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
          
        return count

nums, val = [3, 2, 2, 3],  3
solution = Solution()
result = solution.removeElement(nums, val)
print(result)  # Expected output: 2
print(nums[:result])  # Expected output: [2, 2]