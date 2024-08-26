# https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(open_count, close_count, path, result):
            if open_count == n and close_count == n:
                result.append(path)
                return
            if open_count < n:
                dfs(open_count + 1, close_count, path + "(", result)
            if close_count < open_count:
                dfs(open_count, close_count + 1, path + ")", result)
            return result
        result = []
        dfs(0, 0, "", result)
        return result


n = 3
solution = Solution()
result = solution.generateParenthesis(n)
print(result)
