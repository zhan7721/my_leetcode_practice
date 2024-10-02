# two pointers
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        new_index = 0
        for old_index in range(len(nums)):
            if nums[old_index] != val:
                nums[new_index] = nums[old_index]
                new_index += 1
        return new_index
                
