class Solution:
    def create_pattern(self, s):
        freq_list = [0]*26
        for i in s:
            freq_list[ord(i) - ord('a')] +=1
        char = 'a'
        freq_str = []
        for i in freq_list:
            if i > 0:
               freq_str.append(char)
               freq_str.append(str(i))
            char = chr(ord(char)+1)
        pattern = "".join(freq_str)
        return pattern
    
    def groupAnagram(self,strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for s in strs:
            key = self.create_pattern(s)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())
            
        
        
        
s = Solution()
print(s.groupAnagram(strs = ["eat","tea","tan","ate","nat","bat"]))
        
