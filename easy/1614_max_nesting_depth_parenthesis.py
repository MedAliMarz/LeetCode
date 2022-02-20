class Solution:
    def maxDepth(self, s: str) -> int:
        
        maximum = 0
        count = 0
        for char in s:
            if char == '(':
                count +=1
            
            maximum = max(maximum, count)
            
            if char == ')':
                count -= 1
        return maximum
