class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1 if n== 1 else -1
        trusted = {}
        trusting = [0 for _ in range(n)]
        for a,b in trust :
            if b not in trusted:
                trusted[b] = 1
            else :
                trusted[b] += 1
            trusting[a-1] += 1

        # check if there is a person not trusting anyone

        for index, trustValue in enumerate(trusting) :
            if trustValue == 0 and index+1 in trusted and trusted[index +1] == n-1:
                return index + 1
        return -1
        
