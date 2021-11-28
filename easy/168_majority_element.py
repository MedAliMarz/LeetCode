class Solution:
    def majorityElement(self, nums ) -> int:
        occurencesMap = { }
        maximum = 0
        number = None
        for num in nums:
            if num in occurencesMap:
                occurencesMap[num] += 1
            else:
                occurencesMap[num] = 1
            if number == None or occurencesMap[num] > maximum:
                number = num
                maximum = occurencesMap[num]
        return number
s = Solution()

print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([2,2,1,1,1,1,2,2]))
print(s.majorityElement([2]))
