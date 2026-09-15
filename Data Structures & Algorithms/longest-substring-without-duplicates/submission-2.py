class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = longest = 0

        for char in s:
            while char in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(char)
            longest = max(longest, len(seen))
        return longest

        