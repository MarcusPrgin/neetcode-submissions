class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        curSum = 0
        prev = {0: -1}          

        for i, num in enumerate(nums):
            curSum += num
            remain = curSum % k
            if remain in prev:
                if i - prev[remain] >= 2:
                    return True
            else:
                prev[remain] = i
        return False
        


        
        


        

        