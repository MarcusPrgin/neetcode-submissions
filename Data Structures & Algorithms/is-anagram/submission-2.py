class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        res = {}

        if len(s) != len(t):
            return False
        
        # add s to hashmap
        for i in s: 
            res[i] = res.get(i, 0) + 1
        
        # compare s and t
        for j in t:
            if j not in res:
                return False
            res[j] -= 1
            if res[j] < 0:
                return False

        return True
