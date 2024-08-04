class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if x % 3 == 0:
                continue
            else:
                k += 1
        return k
