class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        candidate = nums[0]; cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate: cnt+=1
            else: cnt-=1
            if cnt == 0: 
                candidate = nums[i]
                cnt = 1
        return candidate

if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([1,1,2,3,4,1,1,1])

