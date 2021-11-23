class Solution:
    def addBinary(self, a:str, b:str):
        return bin((int(a,2) + int(b,2)))[2:]
    def _addBinary(self, a: str, b: str) -> str:
       minlength = min(len(a), len(b))
       maxlength = max(len(a), len(b))
       ret = 0
       arev = a[::-1]
       brev = b[::-1]
       result = ['' for i in maxlength]
       for index in range(length):
            if arev[index] == '0' and brev[index] == '0':
                if ret ==0: 
                    result[index] = '0'
                else:
                    result[index] = '1'
                    ret = 0
            elif arev[index] == '0' or brev[index] == '0':
                if ret == 0:
                    result[index] = '1'
                else:
                    result[index] = '0'
            else:
                if ret == 0:
                    result[index] = '0'
                else:
                    result[index] = '1'
                ret = 3
        

s = Solution()
print(s.addBinary("11","1"))
print(s.addBinary("1010","1011"))
