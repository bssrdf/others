class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        self.combinationSum2Recur(sorted(candidates), target, res, [], 0)
        return res

    def combinationSum2Recur(self, candidates, target, res, cur, start):
        if target == 0 and cur not in res: res.append(cur)
        for i in range(start, len(candidates)):
            if target>=candidates[i]: self.combinationSum2Recur(candidates, target-candidates[i], res, cur+[candidates[i]], i+1)

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5], 8)
    print s.combinationSum2([1,1], 1)