class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        output = [-1]*len(queries)
        for i in range(len(queries)):
            a = queries[i]
            minlen = float('inf')
            for j in range(len(intervals)):
                left, right = intervals[j]
                if left<=a<=right:
                    minlen = min(minlen,right-left+1)
            output[i] = minlen if minlen < float('inf') else -1
        return output