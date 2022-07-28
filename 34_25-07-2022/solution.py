class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1, -1]
        
        for index, value in enumerate(nums):
            if value == target and result[0] == -1:
                result[0] = index
            elif value == target and not result[0] == -1:
                result[1] = index
        
        if result[0] != -1 and result[1] == -1:
            result[1] = result[0]
                
        return result