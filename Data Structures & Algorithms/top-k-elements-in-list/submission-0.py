class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basic idea
        my_dict = {}

        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(my_dict[i][0])

        return res
