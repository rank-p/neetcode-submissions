class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s1, s2 = defaultdict(int), defaultdict(int)

        for c1,c2 in zip(s,t):
            s1[c1] += 1
            s2[c2] += 1
        
        return s1 == s2

        