class Solution:
    def rob(self, nums: List[int]) -> int:
        # value of robbing ith house to the end, alternatively. 
        # base cases are last house value, and second last house value. 
        n = len(nums)
        dp = [0]*n
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-1],nums[n-2])
        for i in range(n-3,-1,-1):
            dp[i] = max(nums[i]+dp[i+2],dp[i+1])
        return dp[0]


# two base cases, with calculations like max are also common and valid. 