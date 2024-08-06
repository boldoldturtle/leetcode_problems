class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        j = {}
        res = 0
        for i in range(len(s)):
            k = 0
            z = 0
            if s[i] not in j.keys():
                j[s[i]] = [i]
                k = 1
            if t[i] not in j.keys():
                j[t[i]] = [i]
                z = 1


            if s[i] in j.keys() and k == 0:
                j[s[i]].append(i)
            if t[i] in j.keys() and z == 0:
                j[t[i]].append(i)
        for k,v in j.items():
            res += abs(v[0]-v[1])
        return res
    
