class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for i in strs: 
            count = [0] * 26

            for j in i:
                index = ord(j) - ord("a")
                count[index] += 1

            key = tuple(count) 
            res[key].append(i) 
        
        return list(res.values())


        