class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = list(bin(n)[2:])
        for index, value in enumerate(binary):
            binary[index] = '0' if value == '1' else '1'
        return int(''.join(binary), 2)
