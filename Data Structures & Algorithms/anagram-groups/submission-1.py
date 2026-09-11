class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            t = tuple(sorted(s))
            m[t].append(s)
        return list(m.values())
