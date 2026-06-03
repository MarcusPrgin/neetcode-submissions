class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = 100000

        for i in nums:
            res = min(res, i)

        return res      