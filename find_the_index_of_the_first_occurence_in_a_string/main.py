# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)

        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1


haystack, needle = "leetcode", "leeto"
solution = Solution()
result = solution.strStr(haystack, needle)
print(result)
