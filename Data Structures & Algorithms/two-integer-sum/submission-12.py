class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []

        for i in range(0, len(nums)):
            c = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == c:
                    res.append(i)
                    res.append(j)
                    return res

        return False

        
        

        
