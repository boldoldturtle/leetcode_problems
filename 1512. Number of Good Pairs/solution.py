class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dicti = {}
        res = 0
        for x in nums:
            if x in dicti.keys():
                dicti[x] += 1
            else:
                dicti[x] = 1
        for k,v in dicti.items():
            res += v*(v-1)//2
        return res
