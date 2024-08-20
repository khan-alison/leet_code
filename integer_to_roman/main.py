class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        roman = []
        for val, sym in zip(values,symbols):
            while num >= val:
                roman.append(sym)
                num -= val
        return ''.join(roman)


num = 3749  
solution = Solution()
result = solution.intToRoman(num)
print(result)