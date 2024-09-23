class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # find target
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1

            while right >= left:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                elif target == nums[mid]:
                    return mid
            return -1
        
        search_index = binary_search(nums, target)
        left, right = search_index, search_index

        # move the pointer to search for range within the nums list
        if left == -1 or right == -1:
            return [-1, -1]
        else:
            while left - 1 >= 0 and nums[left-1] == target:
                left -= 1
            while right + 1 <= len(nums) - 1 and nums[right+1] == target:
                right += 1
            return [left, right]
