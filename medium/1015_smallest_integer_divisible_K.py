class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        max64 = (2**64) - 1

        while n < max64:
            if n%k ==0:
                return len(str(n))

            n = int(str(n) + "1", 10)
        return -1
        

s = Solution()

print(s.smallestRepunitDivByK(1))
print(s.smallestRepunitDivByK(2))
print(s.smallestRepunitDivByK(3))
