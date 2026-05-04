class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0]*(len(nums1)+len(nums2))
        t = len(nums1)+len(nums2)
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        k = 0
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i+=1
            else:
                arr[k] = nums2[j]
                j+=1
            k+=1
        if i < m:
            for e in range(m-i):
                arr[k+e] = nums1[i+e]
        if j < n:
            for e in range(n-j):
                arr[k+e] = nums2[j+e]
        return arr[t//2] if t%2==1 else (arr[t//2]+arr[(t//2)-1])/2
        

