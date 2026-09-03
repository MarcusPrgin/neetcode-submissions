class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        curSum = 0                    
        prev = {0: 1}               
    
        for i in nums:
            curSum += i                          
            count += prev.get(curSum - k, 0)      
            prev[curSum] = prev.get(curSum, 0) + 1 
    
        return count
            