class Solution:
    def productOfArrayExceptSelf(self,nums: list[int]) -> list[int]:
        n = len(nums)
        left = [1]*n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
        right = [1]*n
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
            
        result = [1]*n
        for i in range(n):
            result[i] = left[i] * right[i]
        return result
        
        
s = Solution()
print(s.productOfArrayExceptSelf(nums = [1,2,3,4]))
        
