class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        bijection_words = {}
        bijection_pattern = {}
        for index, char in enumerate(pattern):
            if words[index] not in bijection_words:
                bijection_words[words[index]] = char
            if char not in bijection_pattern:
                bijection_pattern[char] = words[index]

            if words[index] in bijection_words and char in bijection_pattern:
                # verify if both are equal
                if bijection_words[words[index]] != char or bijection_pattern[char] != words[index]:
                    return False
        return True
        



s = Solution()

print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("abc", "b c a"))
