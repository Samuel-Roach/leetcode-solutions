from typing import final


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # counts = [0] * len(matrix)
        # final_list = []

        # for idx, item in enumerate(matrix):
        #     if sum(counts) + len(item) >= k:
        #         # diff = k - sum(counts) - 1
        #         # return item[diff]
        #         final_list.extend(item)
        #         print(f'Final list {final_list}')
        #         return sorted(final_list)[k-1]
        #     final_list.extend(item)
        #     print(f'Final list {final_list}')
        #     counts[idx] += len(item)

        final_list = []

        for item in matrix:
            final_list.extend(item)
        
        return sorted(final_list)[k-1]