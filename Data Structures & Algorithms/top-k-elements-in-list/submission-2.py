class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for (num,count) in m.items():
            buckets[count].append(num)

        res = []
        for bucket in reversed(buckets):
            to_add = bucket[:k]
            res.extend(to_add)
            k -= len(to_add)
            if k == 0:
                return res

        return res