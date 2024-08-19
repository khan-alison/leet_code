class Solution(object):
    def longestPalindrome(self, s):

        if s == s[::-1]:
          return s

        pal = s[0]
        centerL = 0
        centerR = 0
        c = len(s) - 1

        while centerR < c:
          while centerR < c:
            if s[centerR] != s[centerR + 1]: break
            centerR += 1
          i, j = centerL, centerR
          while i > 0 and j < c:
            if s[i - 1] != s[j + 1]: break
            i -= 1
            j += 1
          
          if len(pal) < j - i + 1:
            pal = s[i:j+1]

          centerR += 1
          centerL = centerR
        return pal


s = "cbbd"
solution = Solution()
result = solution.longestPalindrome(s)
print(result)
