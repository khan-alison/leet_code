# https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if not strs:
            return ""

        reversed = sorted(strs)
        first, last = reversed[0], reversed[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result

        # if not strs:
        #     return ""

        # strs.sort()
        # first, last = strs[0], strs[-1]
        # i = 0

        # while i < len(first) and i < len(last) and first[i] == last[i]:
        #     i += 1
        # return first[:i]


strs = ["flower", "flow", "flight"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)
