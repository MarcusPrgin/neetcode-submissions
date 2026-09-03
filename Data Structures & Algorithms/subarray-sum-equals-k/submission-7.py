class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prev = {0 : 1}
        count = 0 
        curSum = 0 

        for i in nums:
            curSum += i
            diff = curSum - k

            if diff in prev:
                count += prev[diff]

            prev[curSum] = prev.get(curSum, 0) + 1
            
        return count











        
        