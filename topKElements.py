class Solution:
    def topKElements(self, nums: list[int], k: int) -> list[int]:
        bucket = [[] for i in range(len(nums) + 1)]  # +1 to avoid index out of range
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        for key, val in hashmap.items():
            bucket[val].append(key)

        result = []
        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for val in bucket[i]:
                    if len(result) >= k:
                        return result
                    result.append(val)

        return result

s = Solution()
print(s.topKElements([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2))
