import heapq
class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []
    def addNum(self, num: int) -> None:
        # they can become uneven. what if. if there even exists a self.right, else push to left first, then transfer.
        if self.right and num > self.right[0]:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left,-1*num)
        if (len(self.left)-len(self.right)) > 1:
            first = -heapq.heappop(self.left)
            heapq.heappush(self.right,first)
        if (len(self.right)-len(self.left)) > 1:
            second = heapq.heappop(self.right)
            heapq.heappush(self.left,-second)
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.right) > len(self.left):
            return self.right[0]
        first = -self.left[0]
        sec = self.right[0]
        return (first+sec)/2
        
        