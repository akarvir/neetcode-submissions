class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        gl = []
        def subsets(i,l):
            if i == len(nums):
                gl.append(l.copy())
                return
            subsets(i+1,l)
            l.append(nums[i])
            subsets(i+1,l)
            l.pop()
        subsets(0,[])
        total = 0 
        for e in gl:
            x = 0
            for k in e:
                x = x^k
            total+=x
        return total
            