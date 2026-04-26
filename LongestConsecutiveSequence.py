class Solution:
    def longestConsecutiveSequence(self,nums: list[int]) -> int:
        hashset = set(nums)
        count = 0
        for i in hashset:
            if i-1 not in hashset:
                length = 0
                while i+length in hashset:
                    length += 1
                count = max(count, length)
        return count
        
s = Solution()
print(s.longestConsecutiveSequence(nums = [100,4,200,1,3,2]))
        
