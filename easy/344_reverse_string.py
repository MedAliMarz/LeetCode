class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s)//2):
            s[index], s[len(s) -index -1] = s[len(s) -index -1], s[index]
s= Solution()
arr = ["h","e","l","l","o"]
s.reverseString(arr)
print(arr)
arr = ["H","a","n","n","a","h"]
s.reverseString(arr)
print(arr)
