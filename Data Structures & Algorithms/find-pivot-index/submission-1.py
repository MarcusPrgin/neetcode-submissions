class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        pivotLeft = 0

        for i in range(len(nums)):
            pivotRight = total - nums[i] - pivotLeft

            if pivotLeft == pivotRight:
                return i
            
            pivotLeft += nums[i]
        
        return -1


            





        

        