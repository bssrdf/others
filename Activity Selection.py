class Solution:
    def maxNumberOfActivities(self, array):
        array.sort(key=lambda x: x.end)
        res = []
        res.append(array[0])
        prev = 0
        for i in range(1, len(array)):
            if array[i].start >= array[prev].end: 
                res.append(array[i])
                prev = i
        return res

    # def dp(self, array):
    #     array.sort(key=lambda x: x.end)
    #     dp = [1 for i in range(len(array))]
    #     for i in range(1, len(array)):             
    #         for j in range(i):
    #             if array[j].end<=array[i].start:
    #                 dp[i] = max(dp[i-1], dp[j]+1)
    #             else:
    #                 dp[i] = max(dp[i-1], dp[i])
    #     return max(dp)

    # def dp(self, array):
    #     array.sort(key=lambda x: x.end)
    #     dp = [1 for i in range(len(array))]
    #     for i in range(1, len(array)):             
    #         for j in range(i):
    #             if array[j].end<=array[i].start:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #             else:
    #                 dp[i] = max(dp[i], dp[j])
    #     return dp[-1]

    def dp(self, array):
        array.sort(key=lambda x: x.end)
        dp = [[array[i]] for i in range(len(array))]
        for i in range(1, len(array)):             
            for j in range(i):
                if array[j].end<=array[i].start:
                    if len(dp[j])+1>len(dp[i]): dp[i] = dp[j][:]+[array[i]]
                else:
                    if len(dp[j])>len(dp[i]): dp[i] = dp[j][:]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    class Interval:
        def __init__(self, start, end):
            self.start = start
            self.end = end
    array = [Interval(1,2), Interval(3,4), Interval(0,6), Interval(5,7), Interval(8,9), Interval(5,9)]
    res = s.maxNumberOfActivities(array)
    for interval in res:
        print interval.start, interval.end
    res = s.dp(array)
    for interval in res:
        print interval.start, interval.end

