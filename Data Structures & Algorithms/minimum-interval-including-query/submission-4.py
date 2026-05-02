import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        copy = sorted(queries)
        res = {}
        h = []
        j = 0
        for i in range(len(copy)):
            a = copy[i]
            res[a] = -1
            while j < len(intervals) and intervals[j][0] <=a :
                left, right = intervals[j][0],intervals[j][1]
                heapq.heappush(h,(right-left+1,right,left)) # added at most once, popped at most once. 
                j+=1
            if not h:
                continue
            while h and h[0][1] < a:
                heapq.heappop(h)
            if h:
                l = h[0][0]
                res[a] = l
        return [res[q] for q in queries]
            

            



            