class Solution:

    def __init__(self):
        
        self.MAP = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
            4 : "IV",
            9 : "IX",
            40 : "XL",
            90 : "XC",
            400 : "CD",
            900 : "CM",}
        self.ARR = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def intToRoman(self, num: int) -> str:
        index = 0
        result = []
        while num != 0 and index < len(self.ARR):
            if num - self.ARR[index] >= 0:
                result.append(self.MAP[self.ARR[index]])
                num -= self.ARR[index]
            else:
                index += 1
        return ''.join(result)

s = Solution()

print(s.intToRoman(3))
print(s.intToRoman(58))
print(s.intToRoman(1994))
