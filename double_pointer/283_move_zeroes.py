class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_pointer = 0
        for fast_pointer in range(len(nums)):
            if nums[fast_pointer] != 0:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
        for i in range(slow_pointer, len(nums)):
            nums[i] = 0