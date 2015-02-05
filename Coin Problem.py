# google

class Solution:
    # minimum number of coins to make change for n
    def minCoin(self, S, n):
        m = len(S)
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(len(S)):
                if i-S[j]>=0: 
                    if not dp[i]: dp[i] = dp[i-S[j]]+1
                    else: dp[i] = min(dp[i], dp[i-S[j]]+1)
        return dp[-1]
    
    # minimum number of coins to make change for n
    def minCoinRecur(self, S, m, n):
        if n<=0: return 0
        if m<=0: return 0
        if m==1: return n
        if n-S[m-1]>=0:
            return min(self.minCoinRecur(S, m-1, n), self.minCoinRecur(S, m, n-S[m-1])+1)
        else:
            return self.minCoinRecur(S, m-1, n)

    # number of ways to make change for n
    def waysCoin(self, S, n):
        dp = [[0 for j in range(len(S)+1)] for i in range(n+1)]
        for j in range(len(S)+1): dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, len(S)+1):
                if S[j-1]<=i:
                    dp[i][j] = dp[i][j-1]+dp[i-S[j-1]][j]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print s.minCoin([1,5,10,25], 100)
    print s.minCoinRecur([1,5,10,25], 4, 100)
    print s.waysCoin([1,5,10,25], 100)
    print s.waysCoin([1,2,3], 4)
