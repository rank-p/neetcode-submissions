class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        v = set(s[0])
        l,r = 0,0
        max_len = 0

        while r < len(s):
            if s[r] in v and l != r:
                v.remove(s[l])
                l += 1
            else:
                max_len = max(max_len, len(s[l:r+1]))
                v.add(s[r])
                r += 1
                
        return max_len

        