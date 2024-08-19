# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 1
        result = 0
        if x < 0:
          a = -1
        
        x = abs(x)
        while x != 0:
          temp = x % 10
          result = result * 10 + temp
          x = x // 10
        if result > pow(2, 31):
          return 0
        return result * a
        
x = 123
solution = Solution()
result = solution.reverse(x)
print(result)