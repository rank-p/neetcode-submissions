class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            t = tuple(sorted(list(tuple(s))))
            m[t].append(s)
        return list(m.values())
