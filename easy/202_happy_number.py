class Solution:
    def isHappy(self, n: int) -> bool:
        old = n
        new = n
        seen = { n :0}
        while new!=1 :
            new = self.digitSquares(old)
            print(old, new)
            if new in seen.keys():
                print(new)
                return False 
            else:
                old = new
                seen[new] = 0
        return True
    def digitSquares(self, n:int) -> int:
        new = 0
        while n != 0:
            new += (n%10)** 2
            n = n//10
        return new

s = Solution()

print(s.isHappy(19))
print(s.isHappy(2))
