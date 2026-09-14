class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])   # sort by start

        result = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if start <= last_end:
                # overlap: extend the last interval's end
                result[-1][1] = max(last_end, end)
            else:
                # no overlap: start a new interval
                result.append([start, end])

        return result