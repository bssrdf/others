class Solution:
    # minimum number of coins to make change for n
    def minCoin(self, S, n):
        m = len(S)
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(len(S)):
                if i-S[j]>=0: dp[i] = min(dp[i], dp[i-S[j]]+1)
        return dp[-1]


    # number of ways to make change for n
    def waysCoin(self, S, n):
        pass

if __name__ == "__main__":
    s = Solution()
    print s.minCoin([1,5,10,25], 100)
    print s.waysCoin([1,5,10,25], 100)