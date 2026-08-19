class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index_map = {} # this maps the value : index, so i[1] = 2 -> 2 : 1
        for i, n in enumerate(nums):
            diff = target - n
            if diff in val_index_map:
                return [val_index_map[diff], i]
            val_index_map[n] = i
        return