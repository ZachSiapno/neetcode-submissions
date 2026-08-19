class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count occurences in each value
        freq = [[] for i in range(len(nums) + 1)]  # index = frequency of element, value = the number that represents the number of frequncy

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num) # adds the value num into the hash table's cnt index

        res = []
        for i in range(len(freq) - 1, 0, -1): # traverse the array in reverse
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
