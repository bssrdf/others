class Solution:
    def isValidPalindrome(self, string1):
        if len(string1) == 0: return True
        i = 0; j = len(string1)-1
        while i<=j:
            while i<len(string1) and (not string1[i].isalnum()): i+=1
            while j<len(string1) and (not string1[j].isalnum()): j-=1
            if string1[i].lower()!=string1[j].lower(): return False
            else:i+=1; j-=1
        return True

if __name__ == "__main__":
    s = Solution()
    print s.isValidPalindrome('A man, a plan, a canal: Panama')
    print s.isValidPalindrome('race a car')