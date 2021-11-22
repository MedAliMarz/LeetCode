class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        index = s.rfind(" ")
        if index == -1:
            return len(s)
        return len(s) - index -1

s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord("   fly me   to   the moon  "))
print(s.lengthOfLastWord("luffy is still joyboy"))
