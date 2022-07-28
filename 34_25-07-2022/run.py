from solution import Solution

s = Solution()

# Example 1
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums=nums, target=target))

# Example 2
target = 6
print(s.searchRange(nums=nums, target=target))

# Example 3
nums = []
target = 0
print(s.searchRange(nums=nums, target=target))