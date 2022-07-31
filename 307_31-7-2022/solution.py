from math import ceil, sqrt

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

        block_size = int(sqrt(len(nums)))
        self.block_store_length = int(ceil(len(nums) / block_size))

        self.block_store = [0] * self.block_store_length
        for i, num in enumerate(nums):
            self.block_store[int(i / self.block_store_length)] += num

    def update(self, index: int, val: int) -> None:
        block = int(index / self.block_store_length)
        self.block_store[block] = self.block_store[block] - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        int_sum = 0
        start_block = int(left / self.block_store_length)
        end_block = int(right / self.block_store_length)

        if start_block == end_block:
            int_sum += sum(self.nums[left:right + 1])
        else:
            # All the block vals
            int_sum += sum(self.block_store[start_block + 1:end_block])
            # All the beginning
            int_sum += sum(self.nums[left:(start_block + 1) * self.block_store_length ])
            # All the end
            int_sum += sum(self.nums[end_block * self.block_store_length:right + 1])

        return int_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)