class Solution:
    alpha = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        if len(s) ==0: return result
        index = 0
        while (index<len(s)):
            if s[index] == 'I' and index +1 < len(s) and (s[index +1] == 'V' or s[index +1] == 'X'):
                result += self.alpha[s[index +1]] - 1
                index += 2
            elif s[index] == 'X' and index+1< len(s) and (s[index +1] == 'L' or s[index +1] == 'C'):
                result += self.alpha[s[index +1]] - 10
                index += 2
            elif s[index] == 'C' and index+1 < len(s) and (s[index +1] == 'D' or s[index +1] == 'M'):
                result += self.alpha[s[index +1]] - 100
                index +=2
            else:
                result += self.alpha[s[index]]
                index += 1
        return result





s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
