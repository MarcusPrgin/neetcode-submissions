class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        curSum = 0
        count = 0
        prefixCount = {0: 1}

        for n in nums:
            curSum += n
            remain = curSum % k

            count += prefixCount.get(remain, 0)
            prefixCount[remain] = prefixCount.get(remain, 0) + 1

        return count


            




        
        