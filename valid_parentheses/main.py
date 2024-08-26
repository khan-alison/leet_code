# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = []

        for char in s:
            if char in hash_map:
                stack.append(char)
            else:
                if not stack or hash_map[stack.pop()] != char:
                    return False
        return len(stack) == 0
        # def dfs(i, s):
        #     if i == len(s):
        #         return len(stack) == 0
        #     if s[i] in hash_map:
        #         stack.append(s[i])
        #     else:
        #         if not stack or hash_map[stack.pop()] != s[i]:
        #             return False

        #     return dfs(i + 1, s)

        # return dfs(0, s)


s = "()[]{}"
solution = Solution()
result = solution.isValid(s)
print(result)
