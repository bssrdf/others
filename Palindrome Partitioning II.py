class Solution:
    def minCut(self, s):
        dp = [0 for i in range(len(s))]
        