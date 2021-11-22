#TODO: check & resubmit , got tle with [1,1]

class Solution:
    def removeDuplicates(self, nums) -> int:
        dupsNumber = 0
        for index in range(len(nums)-1):
            number = nums[index]
            if (index+1 + dupsNumber == len(nums)):
                break
            while index+1 < len(nums) and nums[index +1] == number:
                dupsNumber += 1
                for curr in range(index+1, len(nums)-1):
                    nums[curr] = nums[curr +1]
        return len(nums) - dupsNumber
                


s = Solution()
arr = [1,1,2]
print(s.removeDuplicates(arr), arr)
arr = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(arr), arr)
