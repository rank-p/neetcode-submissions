class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        #1,2,3,4,5,6
        #6,1,2,3,4,5
        #5,6,1,2,3,4
        #4,5,6,1,2,3
        #3,4,5,6,1,2
        #2,3,4,5,6,1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            




        