class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        prev = {}
        l = 0 
        maxFreq = 0 
        longest = 0 

        for r, v in enumerate(s):

            prev[v] = prev.get(v, 0) + 1
            maxFreq = max(maxFreq, prev[v])

            while (r - l +1) - maxFreq > k:
                prev[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest






        


                
                    


            
            

                








        