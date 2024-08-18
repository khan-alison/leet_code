class Solution(object):
    def longestPalindrome(self, s):

        if s == s[::-1]:
            return s

        c = len(s)-1
        cenLeft, cenRight = 0, 0
        pal = s[0]

        while cenRight < c:
            while cenRight < c:
                if s[cenRight] != s[cenRight + 1]:
                    break
                cenRight = cenRight + 1
            i, j = cenLeft, cenRight
            while i > 0 and j < c:
                if s[i - 1] != s[j + 1]:
                    break
                i -= 1
                j += 1
            if len(pal) < j + 1 - i:
                pal = s[i:j+1]
            cenRight = cenRight + 1
            cenLeft = cenRight
        return pal


s = "babad"
solution = Solution()
result = solution.longestPalindrome(s)
print(result)
