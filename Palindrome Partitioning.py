# leetcode

class Solution:
    def partition(self, s):
        res = []
        self.partitionRecur(s, [], res)
        return res

    def partitionRecur(self, s, cur, res):
        if len(s)==0: res.append(cur); return
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]): self.partitionRecur(s[i+1:], cur[:]+[s[:i+1]], res)

    def isPalindrome(self, s):
        if len(s) == 0: return True
        i = 0; j = len(s)-1
        while i<=j:
            if s[i]!=s[j]: return False
            i+=1; j-=1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.partition("aab")

