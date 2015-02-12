class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        lookup = {}; longest = 0; curr=0
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = i
                curr+=1
            else:
                curr = min(i-lookup[s[i]], curr+1)
                lookup[s[i]]=i
            longest = max(longest, curr)
        return longest

if __name__ == "__main__":
    s = Solution()
    print s.lengthOfLongestSubstring('tmmzuxt')