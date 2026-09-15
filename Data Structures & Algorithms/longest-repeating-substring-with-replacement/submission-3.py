class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = longest = 0

        for r, char in enumerate(s):
            counts[char] += 1
        
            while (r-l+1 - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r-l+1))
        
        return longest

            