class Solution:
    def divisorGame(self, n: int) -> bool:
        
        # o => Alice turn
        # 1 => Bob turn
        
        memo = {}
        return self.divisorGameTurn(n, 0, memo={})
    def divisorGameTurn(self, n: int, turn, memo) -> bool:

        if n in memo :
            return memo[n]
        
        
        xs = [self.divisorGameTurn(n- i, 1-turn, memo )  for i in range(1, n) if n%i == 0]
        
        if len(xs) == 0:
            memo[n] = turn == 1
        else:
            memo[n] = any(xs) and turn == 0
        
        return memo[n]
        
        
