class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        else:
            maxn = 1
            arr = [0, 1]
            for index in range(2, n+1):
                
                if index %2 == 0:
                    val = arr[index//2]
                else:
                    val = arr[index//2] + arr[1+ (index//2)]
                
                arr.append(val)
                
                maxn = max(maxn, val)
            return maxn
