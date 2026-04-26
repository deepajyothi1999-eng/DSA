class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
        
        
s = Solution()
print(s.containsDuplicates(nums = [2, 7, 11, 15]))
