class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2 :
            return 1
        old = 0
        mid = 1
        new = 1
        for index in range(2,n):
        
            old, mid, new = mid, new, old+mid+new
            
        return new
