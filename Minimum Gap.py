# opposite of Maximum Gap on leetcode

class Solution:
    # @param num, a list of integer
    # @return a list of pair of integers
    def minimumGap(self, num):
        if len(num)<2: return 0
        maxLength = len(str(max(num)))
        strNum = [str(i)[::-1] for i in num]
        for i in range(maxLength):
            buckets = [[] for j in range(10)]
            for k in strNum:
                if len(k)<=i:
                    buckets[0].append(k)
                else:
                    buckets[int(k[i])].append(k)
            strNum = []
            for j in range(10):
                strNum.extend(buckets[j])
        num = [int(i[::-1]) for i in strNum]
        minGap = 9223372036854775807
        for i in range(1, len(num)):
            minGap = min(minGap, num[i]-num[i-1])
        res = []
        for i in range(1, len(num)):
            if num[i]-num[i-1] == minGap:
                res.append((num[i-1], num[i]))
        return res

if __name__ == "__main__":
    s = Solution()
    print s.minimumGap([1,3,5,7,11])