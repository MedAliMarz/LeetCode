class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while result//10 != 0:
            temp = 0
            while result!=0:
                temp += result%10
                result = result//10
            result = temp
        return result
s = Solution()
print(s.addDigits(38))
