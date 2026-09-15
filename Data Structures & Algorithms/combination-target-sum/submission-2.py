class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(elems, current_sum, i):
            if current_sum == target:
                res.append(elems.copy())
                return
            if i >= len(nums) or current_sum > target:
                return
            
            elems.append(nums[i])
            dfs(elems, current_sum + nums[i], i)
            elems.pop()
            # skip the number
            dfs(elems, current_sum, i+1)

        
        dfs([],0,0)
        return [list(x) for x in res]


            
