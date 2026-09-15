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
            if nums[l] < nums[mid] < nums[r]:
                #1,2,3,4,5,6
                r = mid - 1
            elif nums[mid] < nums[l]:
                #6,1,2,3,4,5
                #5,6,1,2,3,4
                #4,5,6,1,2,3
                r = mid
            elif nums[mid] > nums[r]:
                #3,4,5,6,1,2
                #2,3,4,5,6,1
                l = mid + 1
            else:
                print(nums, l, mid, r)
                r = mid
        return nums[l]
            




        