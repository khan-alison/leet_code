# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s):
        s, result, index, sign = s.strip(), 0, 0, 1

        if len(s) == 0:
            return 0

        if s[index] == "+":
            sign = 1
            index += 1
        elif s[index] == "-":
            sign = -1
            index += 1

        while index < len(s):
            if not s[index].isdigit():
                break

            result = result * 10 + int(s[index])

            if result > (2**31 -1):
              return -2**31 if sign == -1 else 2**31 -1
            index += 1
        return result * sign

        # s, result, index, sign = s.strip(), 0, 0, 1

        # if len(s) == 0:
        #     return 0

        # if s[index] == "+":
        #     sign = 1
        #     index += 1
        # elif s[index] == "-":
        #     sign = -1
        #     index += 1

        # while index < len(s):
        #     if not s[index].isdigit():
        #         break
        #     print(result)
        #     print((2**31 - 1 - int(s[index])) // 10)

        #     if result > (2**31 - 1 - digit) // 10:
        #         return -2**31 if sign == -1 else 2**31 - 1

        #     result = result * 10 + int(s[index])
        #     index += 1
        # return result * sign


s = "21474836460"
s ="   -042"
solution = Solution()
result = solution.myAtoi(s)
print(result)
