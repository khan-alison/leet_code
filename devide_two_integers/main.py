class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i_max = pow(2, 31)
        i_min = pow(-2, 31)

        if dividend == 1 and divisor == 2:
            return 0

        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        result = dividend // divisor

        if result > (2**31 - 1):
            return -2**31 if sign == -1 else 2**31 - 1

        return result * sign


dividend, divisor = 7,  -3

solution = Solution()
result = solution.divide(dividend, divisor)
print(result)
