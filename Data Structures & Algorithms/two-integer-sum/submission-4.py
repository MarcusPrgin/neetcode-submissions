class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []

        for i in range(len(nums)): 
            compliment = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == compliment:
                    res.append(i)
                    res.append(j)

                    return res