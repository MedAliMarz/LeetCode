class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        rows = [ [] for num in range(numRows)]
        direction = -1
        index = 0
        for char in s:
            rows[index].append(char)
            if index == 0 or index == numRows -1:
                direction *= -1
            index += direction
        
        return ''.join([''.join(row) for row in rows])


s = Solution()

print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
