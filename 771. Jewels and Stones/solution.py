class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = {}
        for i in range(len(jewels)):
            j[jewels[i]] = 0
        for i in range(len(stones)):
            if stones[i] in j.keys():
                j[stones[i]] += 1
        return sum(j.values())

    
