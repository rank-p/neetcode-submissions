class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ms, mt = defaultdict(int), defaultdict(int)
        for (s,t) in zip(s,t):
            ms[s] += 1
            mt[t] += 1
        return ms == mt


        
        