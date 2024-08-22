# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits):
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backTrack(i, currentValue):
            if i == len(digits):
                res.append(currentValue)
                return
            for c in keyboard[digits[i]]:
                backTrack(i + 1, currentValue + c)

        if digits:
            backTrack(0, "")

        return res


digits = "23"
solution = Solution()
result = solution.letterCombinations(digits)
print(result)
