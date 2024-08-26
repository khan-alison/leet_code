# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[:] = sorted(set(nums))
        # return len(nums)
        i = 0
        for k in range(1, len(nums)):
          if nums[i] != nums[k]:
            i += 1
            nums[i] = nums[k]
        return i + 1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
result = solution.removeDuplicates(nums)
print(result)
