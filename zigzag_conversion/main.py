# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        # currentRow = 0
        # direction = False
        index, step = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step

        return "".join(rows)


s = "PAYPALISHIRING"
solution = Solution()
result = solution.convert(s, 4)
print(result)
