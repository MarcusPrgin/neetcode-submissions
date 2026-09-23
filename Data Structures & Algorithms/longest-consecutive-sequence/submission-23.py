class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        longest = 0 

        for n in num:
            length = 0
            if n-1 not in num:
                while n + length in num:
                    length += 1

            longest = max(longest, length)
        
        return longest
