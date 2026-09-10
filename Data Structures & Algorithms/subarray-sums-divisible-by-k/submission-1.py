class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        res = 0 

        for i in range(len(nums)):
            curSum = 0 

            for j in range(i, len(nums)):
                curSum += nums[j]

                if curSum % k == 0:
                    res += 1
        
        return res
        

            




        
        