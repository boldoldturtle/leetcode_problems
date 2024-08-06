class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for x in accounts:
            z = sum(x)
            if z > maxi:
                maxi = z
        return maxi
