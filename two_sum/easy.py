class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, value in enumerate(nums):
            complement = target - value 
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[value] = index
        return []

        



solution = Solution()
nums =  [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(result)
        
