class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        reset = 0
        for num in nums:
            if num == 0:
                reset = max(reset, count)
                count = 0
            else:
                count += 1
        return max(count, reset)