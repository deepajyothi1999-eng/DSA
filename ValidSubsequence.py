class Solution:
    def validSubsequence(self,s: str, t:str) -> bool:
        itr1, itr2 = 0, 0
        while itr1 < len(s) and itr2 < len(t):
            if s[itr1] == t[itr2]:
                itr2 += 1
                itr1 += 1
            else:
                itr2 += 1
        if itr1 == len(s):
            return True
        return False
        
        
        
s = Solution()
print(s.validSubsequence(s = "abc", t = "ahbgdc"))
        
