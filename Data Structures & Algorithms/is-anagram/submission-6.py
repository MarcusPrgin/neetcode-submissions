class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        res = {}

        if len(s) != len(t):
            return False

        for i in s: 
            res[i] = res.get(i, 0) + 1
        
        for i in t:
            if i not in s: 
                return False
            res[i] -= 1

            if res[i] < 0:
                return False

        return True


