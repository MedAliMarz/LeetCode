class Solution:
    def fib(self, n: int) -> int:
        array = [0, 1]
        
        for i in range(2, n+1):
            array.append(array[i-1] + array[i-2])
        
        return array[n]

