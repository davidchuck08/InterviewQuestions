class Solution:
    def longestSubstringWithoutRepeatingChar(self, s):
        ans = 0
        start = 0
        end = 0
        charDic = {}
        for c in s:
            end+=1
            if c in charDic.keys():
                start+=1
            charDic[c]=1
            ans = max(ans,end-start)
        
        print ans
                

if __name__ == '__main__':
    sol = Solution()
    sol.longestSubstringWithoutRepeatingChar('abcd
    abcabc')