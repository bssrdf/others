class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.combinationSumRecur(sorted(candidates), target, res, [], 0)
        return res

    def combinationSumRecur(self, candidates, target, res, cur, start):
        if target == 0: res.append(cur)
        for i in range(start, len(candidates)):
            if (target - candidates[i]) >= 0: self.combinationSumRecur(candidates, target-candidates[i], res, cur+[candidates[i]], i) 

if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2,3,6,7], 7)
    print s.combinationSum([1,2,3,4,5], 5)