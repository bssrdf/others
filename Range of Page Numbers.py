class Solution:
    def rangeOfPages(self, d, k):
        PgNoLowerBound = 0; PgNoUpperBound = 0;
        current = 1; cnt = 0
        while current!=0:
            if str(d) in str(current): cnt+=str(current).count(str(d))
            if PgNoLowerBound == 0 and cnt == k: PgNoLowerBound = current
            if cnt == k: PgNoUpperBound = current
            if cnt>k: break
            current+=1
        return (PgNoLowerBound, PgNoUpperBound)

if __name__ == "__main__":
    s = Solution()
    print s.rangeOfPages(4, 1)
    print s.rangeOfPages(4, 0)
