class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total = sum(nums)
        remain = total % p

        if remain == 0: 
            return 0
        
        res = len(nums)
        remain_to_index = {0 : -1}
        curRemain = 0 

        for i, n in enumerate(nums):
            curRemain = (curRemain + n) % p
            prefix = (curRemain - remain + p) % p

            if prefix in remain_to_index:
                length = i - remain_to_index[prefix] 
                res = min(res, length)
            
            remain_to_index[curRemain] = i

        return -1 if res == len(nums) else res