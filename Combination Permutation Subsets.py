# leetcode

import math

class Solution:
    # input are unique numbers
    def permutation(self, nums):
        if len(nums)==0: return [[]]
        nums.sort()
        res = []
        for i in range(len(nums)):
            remains = self.permutation(nums[:i]+nums[i+1:])
            for remain in remains:
                res.append(remain+[nums[i]])
        return res

    # input contain duplicates
    def permutation2(self, nums):
        if len(nums)==0: return [[]]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i==0 or nums[i]!=prev:
                prev = nums[i]
                remains = self.permutation2(nums[:i]+nums[i+1:])
                for remain in remains: res.append(remain+[nums[i]])
            else: continue
        return res

    # input are unique numbers
    def subsets(self, nums):
        if len(nums) == 0: return [[]]
        nums.sort()
        currents = [[]]
        for num in nums:
            next = []
            for cur in currents:
                next.append(cur[:])
                next.append(cur+[num])
            currents = next
        return currents

    # input contain duplicates
    def subsets2(self, nums):
        if len(nums) == 0: return [[]]
        nums.sort()
        currents = [[]]
        for num in nums:
            next = []
            for cur in currents:
                if (cur[:]) not in next: next.append(cur[:])
                if (cur+[num]) not in next: next.append(cur+[num])
            currents = next
        return currents

    # input are unique numbers
    def combination(self, n, k):
        return self.combinationRecur(range(1, n+1), k)

    def combinationRecur(self, nums, k):
        if k==0: return [[]]
        if k==len(nums): return [nums[:]]
        res = []
        for i in range(len(nums)):
            remains = self.combinationRecur(nums[i+1:], k-1)
            for remain in remains: res.append([nums[i]]+remain)
        return res

    # input are unique numbers
    def getPermutation(self, n, k):
        nums = range(1, n+1); k = k-1
        fact = math.factorial(n-1)
        res = ''
        for j in reversed(range(n)):
            i = k/fact
            res = res+str(nums[i])
            del nums[i]
            k = k%fact
            if j>0: fact = fact/j
        return res

    # input are unique numbers
    def nextPermutation(self, nums):
        if len(nums)==1: return nums
        i = len(nums)-2
        while i>=0:
            if nums[i]>=nums[i+1]: i-=1
            else: break
        if i==-1: return list(reversed(nums))
        j = len(nums)-1
        while j>i:
            if nums[j]>nums[i]: break
            else: j-=1
        nums[i], nums[j] = nums[j], nums[i]
        return nums[:i+1]+list(reversed(nums[i+1:]))

if __name__ == "__main__":
    s = Solution()
    print s.permutation([1,2,3])
    print s.permutation2([1,1,2])
    print s.subsets([1,2,3])
    print s.subsets2([1,1,2])
    print s.combination(4,2)
    print s.getPermutation(4,2)
    print s.nextPermutation([2,3,1])