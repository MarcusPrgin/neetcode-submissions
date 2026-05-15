class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # val : index

        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in prevmap:
                return [prevmap[compliment], i]
            
            prevmap[n] = i
        return