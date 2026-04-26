class Solution:
    def validAnagram(self,s: str, t:str) -> bool:
        bucket = [0]*26
        for i in s:
            bucket[ord(i) - ord('a')] += 1
        for i in t:
            bucket[ord(i)-ord('a')] -= 1
        for i in bucket:
            if i!= 0:
                return False
        return True
        
        
        
s = Solution()
print(s.validAnagram(s = "anagram", t = "nagaram"))
        
