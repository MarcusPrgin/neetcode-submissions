class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counts = {}
        l = 0
        need = {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        for r in range(len(s2)):
            counts[s2[r]] = counts.get(s2[r], 0) + 1

            while (r - l + 1) > len(s1):
                counts[s2[l]] -= 1

                if counts[s2[l]] == 0:
                    del counts[s2[l]]
                
                l += 1
            
            if need == counts:
                return True
        
        return False

        