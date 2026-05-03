class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        new_nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*(n+2) for _ in range(n+2)]
        for l in range(n,0,-1):
            for r in range(l,n+1):
                for i in range(l,r+1):
                    a = new_nums[l-1]*new_nums[r+1]*new_nums[i]
                    dp[l][r] = max(dp[l][r],a+dp[l][i-1]+dp[i+1][r])
        return dp[1][n]
                    

