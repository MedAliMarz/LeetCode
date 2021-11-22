class Solution:
    def plusOne(self, digits):
        digits.reverse()
        if digits[0] != 9:
            digits[0] += 1
        else:
            index = 0
            while index < len(digits) and digits[index] ==9:
                digits[index] = 0
                index += 1
            if index < len(digits):
                digits[index] += 1
            else:
                digits.append(1)
        digits.reverse()
        return digits
        digits[0]


s = Solution()
print(s.plusOne([1,2,3]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([0]))
print(s.plusOne([9]))
