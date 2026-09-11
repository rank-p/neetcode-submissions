class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            m[key].append(s)
            
        
        return list(m.values())
        