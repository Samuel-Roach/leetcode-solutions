from solution import Solution

s = Solution()

# Example 1
print(s.kthSmallest(matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8))

# Example 2
print(s.kthSmallest(matrix=[[-5]], k=1))

# Test Example 1
print(s.kthSmallest(matrix=[[1,2],[1,3]], k=2))