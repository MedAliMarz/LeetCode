class Solution:
    def removeElement(self, nums, val: int) -> int:
        dups = 0
        for index, number in enumerate(nums):
            if number == val:
                while nums[index] == val:
                    if dups == len(nums):
                        return 0
                    if dups + index +1 == len(nums):
                        return len(nums) - dups - 1
                    dups += 1
                    for curr in range(index, len(nums)-1):
                        nums[curr] = nums[curr +1]
        return len(nums) - dups
        
s = Solution()
arr = [3,2,2,3]
print(s.removeElement(arr, 3), arr)
arr = [0,1,2,2,3,0,4,2]
print(s.removeElement(arr, 2), arr)
