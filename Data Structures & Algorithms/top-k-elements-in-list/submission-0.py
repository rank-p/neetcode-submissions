class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        x= list(m.items())
        x.sort(key=lambda x: x[1], reverse=True)
        return [x[t][0] for t in range(k)]