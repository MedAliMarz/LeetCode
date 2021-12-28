class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteMap = self.mapString(ransomNote)
        magazineMap = self.mapString(magazine)
        for key in noteMap.keys():
            if key not in magazineMap or noteMap[key]> magazineMap[key]:
                return False
        return True
    def mapString(self, string: str):
        tempMap = {}
        for char in string:
            if char in tempMap:
                tempMap[char] += 1
            else:
                tempMap[char] = 1
        return tempMap
s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))
