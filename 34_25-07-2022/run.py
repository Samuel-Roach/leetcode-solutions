from solution import Solution

s = Solution()

nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums=nums, target=target))

target = 6
print(s.searchRange(nums=nums, target=target))

nums = []
target = 0
print(s.searchRange(nums=nums, target=target))