class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        
        start1 = self.minCostClimbingTemp(cost, 1, memo)
        start0 = self.minCostClimbingTemp(cost, 0, memo)
        
        return min(start1, start0)
    
    def minCostClimbingTemp(self, cost: List[int], index, memo) -> int:
        if index in memo:
            return memo[index]
        
        if index < len(cost):
            
            memo[index] = cost[index] + min(self.minCostClimbingTemp(cost, index + 1, memo),self.minCostClimbingTemp(cost, index + 2, memo))
        
            return memo[index]
        else:
            return 0
