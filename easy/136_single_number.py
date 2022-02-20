class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        print("~~~")
        for num in nums:
            print(result)
            result ^= num
        return result

s = Solution()

print(s.singleNumber([2,2,1]))

print(s.singleNumber([4,1,2,1,2]))

print(s.singleNumber([1]))
print(s.singleNumber([-2,-2,1]))

