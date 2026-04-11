class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basic idea
        my_dict = {}

        # time O(n), space O(n)
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        # time O(nlogn), space O(n)
        my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        res = []
        # time O(n), space O(n)
        for i in range(k):
            res.append(my_dict[i][0])
        # =>time O(nlogn), O(n)
        return res
