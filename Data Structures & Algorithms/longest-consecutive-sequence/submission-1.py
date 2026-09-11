class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for n in nums:
            if n-1 not in s:
                l = 0
                while n in s:
                    l += 1
                    n += 1
                max_len = max(max_len, l)
        
        return max_len

        