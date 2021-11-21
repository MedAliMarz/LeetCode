class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for index in range(len(s)//2):
            if s[index] != s[len(s)-index-1]:
                return False
        return True 


# testing

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(123))
print(s.isPalindrome(10))
print(s.isPalindrome(-101))
