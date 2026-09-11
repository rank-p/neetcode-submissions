class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        
        freq = [[] for _ in range(len(nums)+1)]
        for (n, count) in m.items():
            freq[count].append(n)
        
        res = []
        for bucket in reversed(freq):
            to_add = bucket[:k]
            res.extend(to_add)

            k -= len(to_add)
            if k == 0:
                return res
        
        raise ValueError()

        
        