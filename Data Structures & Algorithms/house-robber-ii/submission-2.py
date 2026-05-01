class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        first = [0]*(len(nums)-1)
        second = [0]*(len(nums)-1)
        first[n-2] = nums[n-2]
        first[n-3] = max(nums[n-2],nums[n-3])
        for i in range(n-4,-1,-1):
            first[i] = max(nums[i]+first[i+2],first[i+1])
        second[n-2] = nums[n-1]
        second[n-3] = max(nums[n-2],nums[n-1])
        for i in range(n-4,-1,-1):
            second[i] = max(nums[i+1]+second[i+2],second[i+1])
        return max(second[0],first[0])
        
