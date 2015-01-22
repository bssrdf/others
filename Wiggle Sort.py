# http://www.fgdsb.com/2015/01/20/special-sorting/
class Solution:
    def sort(self, nums):
        if len(nums) == 0: return
        current = nums[0]; flag = True # a <= b
        for i in range(len(nums)-1):
            if (flag and current>nums[i+1]) or (not flag and current<nums[i+1]):
                nums[i] = nums[i+1]
            else:
                nums[i] = current
                current = nums[i+1]
            flag = not flag
        nums[len(nums)-1] = current

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    print nums
    s.sort(nums)
    print nums


