# leetcode

class Solution:
    def decodeWays(self, string1):
        if len(string1) == 0: return 0
        dp = [0 for i in range(len(string1)+1)]
        dp[0] = 1
        for i in range(1, len(dp)):
            if string1[i-1] >= '1' and string1[i-1] <= '9': dp[i] += dp[i-1]
            if i>=2 and string1[i-2:i] >='10' and string1[i-2:i] <= '26': dp[i] += dp[i-2]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print s.decodeWays("011")
    print s.decodeWays("")
    print s.decodeWays("1")
    print s.decodeWays("10")

