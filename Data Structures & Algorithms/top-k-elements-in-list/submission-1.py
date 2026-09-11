class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for (num, count) in m.items():
            buckets[count].append(num)
        
        res = []
        for bucket in reversed(buckets):
            adding = bucket[:k]
            res.extend(adding)
            k -= len(adding)
            if k == 0:
                return res
        return res