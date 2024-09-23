class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        if mid == right:
            # this covers the situation where target is bigger than any number 
            # now mid points at the last number index, target goes to the next index
            return mid + 1
        else:
            # for other situations where the target is missing, 
            # mid points at the left number index, which is also the insertion position
            return mid