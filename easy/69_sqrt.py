class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        return self.binarySearchIter( x)
    def binarySearch(self, low, high, target):
        mid = (low + high)  // 2
        if mid **2 <= target and (mid+1) **2 > target:
            return mid
        elif mid **2 > target:
            return self.binarySearch(low, mid -1, target)
        elif mid ** 2 < target:
            return self.binarySearch(mid +1, high, target)
    def binarySearchIter(self, target):
        low = 0
        high = target //2
        found = False
        result = None
        while not found:
            mid = (high + low)//2
            if mid **2 <= target and (mid+1) **2 > target:
                found = True
                return mid
            elif mid **2 > target:
                high = mid - 1
            elif mid ** 2 < target:
                low = mid + 1

s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(2147395599))
