class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = 0
        for i, num in enumerate(nums):
            if num < 0:
                neg = i
            else:
                break

        sorted_list = []
        pos = neg + 1
        while neg >= 0 or pos < len(nums):
            if neg < 0:
                sorted_list.append(nums[pos] * nums[pos])
                pos += 1
            elif pos >= len(nums):
                sorted_list.append(nums[neg] * nums[neg])
                neg -= 1 
            elif nums[neg] * nums[neg] > nums[pos] * nums[pos]:
                sorted_list.append(nums[pos] * nums[pos])
                pos += 1
            elif nums[neg] * nums[neg] < nums[pos] * nums[pos]:
                sorted_list.append(nums[neg] * nums[neg])
                neg -= 1 
            elif nums[neg] * nums[neg] == nums[pos] * nums[pos]:
                sorted_list.append(nums[neg] * nums[neg])
                neg -= 1  
                sorted_list.append(nums[pos] * nums[pos])
                pos += 1   
        return sorted_list


        



        