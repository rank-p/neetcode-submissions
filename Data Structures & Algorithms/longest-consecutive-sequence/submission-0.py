class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for n in nums:
            if n-1 not in s:
                l = 1
                c = n+1
                while c in s:
                    l += 1
                    c += 1
                max_len = max(l, max_len)
        return max_len

        