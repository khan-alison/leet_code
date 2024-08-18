class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        start = 0
        result = 0
        for i, char in enumerate(s):
          if char in hash_map and hash_map[char] >= start:
            start = hash_map[char] + 1
          hash_map[char] = i
          result = max(result, i - start + 1)
        return result


s1 = "abcabcbb"
s2 = "pwwkew"
solution = Solution()
result1 = solution.lengthOfLongestSubstring(s1)
result2 = solution.lengthOfLongestSubstring(s2)

print(result1)
print(result2)
