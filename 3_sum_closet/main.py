# https://leetcode.com/problems/3sum-closest/
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(result - target):
                    result = total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return result


nums, target = [-1, 2, 1, -4], 1
solution = Solution()
result = solution.threeSumClosest(nums, target)
print(result)
