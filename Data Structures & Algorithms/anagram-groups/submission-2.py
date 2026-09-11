class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        base = ord("a")
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char)-base] += 1
            m[tuple(counts)].append(s)
        return list(m.values())
