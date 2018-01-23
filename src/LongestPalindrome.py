class Palindrome:
    def __init__(self, s):
        self.s = s

    def longestPalindrome(self):
        res = ""
        for i in range(len(self.s)):
            temp = self.helper(i,i, self.s)
            if len(temp) > len(res):
                res= temp
            temp = self.helper(i,i+1, self.s)
            if len(temp) > len(self.s):
                res = temp  
        return res
        
    def helper(self, l, r, s):
        while l>=0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
if __name__ == '__main__':
    test = Palindrome('ababaaab')
    print test.longestPalindrome()


