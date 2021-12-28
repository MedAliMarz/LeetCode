class Solution:
    def reverse(self, x: int) -> int:
        signed = x < 0
        stringified = str( x *-1 if signed else x )
        stringified_reversed = stringified[::-1]
        number_reversed = int(stringified_reversed, 10)

        result = number_reversed * -1 if signed else number_reversed
        if result > (2**31) -1 or result < -1* (2**31):
            return 0
        else:
            return result
    
s = Solution()
print(s.reverse(123))
print(s.reverse(-321))
