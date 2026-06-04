class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target: return m

            if nums[m]>target and nums[m]>=nums[0] and target<nums[0]:
                l = m+1
            elif nums[m]>target or (nums[m]<nums[0] and target>nums[-1]):
                r = m-1
            elif nums[m]>=nums[0] or target<=nums[-1]:
                l = m+1
        return -1