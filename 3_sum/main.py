# https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # hash_map = {}
        # result = []

        # def append_triplet(triplet):
        #     return result.append(triplet)

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for h in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[h] == 0:
        #                 triplet = tuple(sorted([nums[i], nums[j], nums[h]]))
        #                 if triplet not in hash_map:
        #                     hash_map[triplet] = triplet
        #                     append_triplet(list(triplet))
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)
