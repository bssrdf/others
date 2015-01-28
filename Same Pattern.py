# dropbox
# pattern is abab, target is redblueredblue, return True
# pattern is aabb, target is xyzabcxyzabc, return False

class Solution:
    def isSamePattern(self, pattern, target):
        if len(pattern)>len(target): return False
        return self.isSamePatternRecur(pattern, 0, target, 0, {})

    def isSamePatternRecur(self, pattern, pIdx, target, tIdx, lookup):
        if (pIdx == len(pattern)) and (tIdx == len(target)): return True
        if (pIdx == len(pattern)) or (tIdx == len(target)): return False
        if pattern[pIdx] in lookup:
            toMatch = lookup[pattern[pIdx]]
            if ((tIdx+len(toMatch))>len(target)) or target[tIdx:tIdx+len(toMatch)] != toMatch: return False
            else: return self.isSamePatternRecur(pattern, pIdx+1, target, tIdx+len(toMatch), lookup)
        else:
            for i in range(tIdx, len(target)):
                lookup[pattern[pIdx]] = target[tIdx:i+1]
                res = self.isSamePatternRecur(pattern, pIdx+1, target, i+1, lookup)
                del lookup[pattern[pIdx]]
                if res: return True
        return False

if __name__ == "__main__":
    s = Solution()
    print s.isSamePattern('abab', 'redblueredblue')
    print s.isSamePattern('aaaa', 'xyzxyzxyzxyz')
    print s.isSamePattern('aabb', 'xyzabcxyzabc')