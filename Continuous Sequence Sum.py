class Solution:
    def searchSeq(self, nums, target):
        nums.sort()
        if len(nums) == 0: return False
        i = 0; j = 0
        while i<=j and j<=len(nums):
            if i == j: j+=1
            elif i<j and sum(nums[i:j]) == target: return True
            elif i<j and sum(nums[i:j]) < target: j+=1
            elif i<j and sum(nums[i:j]) > target: i+=1
        return False

if __name__ == "__main__":
    s = Solution()
    print s.searchSeq([1,2,3,4,5], 9)
    print s.searchSeq([1,2,3,4,5], 3)
    print s.searchSeq([1,2,3,4,5], 8)        