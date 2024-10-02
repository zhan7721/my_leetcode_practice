class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow = 0
        result = 1e10
        current_sum = 0
        for fast in range(len(nums)):
            current_sum += nums[fast]
            while target <= current_sum and slow <= fast:
                result = min(result, fast - slow + 1)
                current_sum -= nums[slow]
                slow += 1
        if result == 1e10:
            return 0
        else:
            return result
