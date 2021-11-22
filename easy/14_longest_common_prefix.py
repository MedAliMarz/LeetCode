class Solution:
    def longestCommonPrefix(self, strs) -> str:
        index = 0
        common = ""
        minLength = min([len(string) for string in strs])
        while True:
            if index >= minLength:
                return common
            char = strs[0][index]
            for s_index in range(1,len(strs)):
                if strs[s_index][index] != char:
                    return common
            index += 1
            common += char
        return common


s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
