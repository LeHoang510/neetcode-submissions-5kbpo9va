class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basic idea
        my_dict = {}

        # time O(n), space O(n)
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1

        # time O(n), space O(n)
        my_list = [[] for i in range(len(nums)+1)]

        # time O(n)
        for key, val in my_dict.items():
            my_list[val].append(key)
        
        res = []
        # time O(n)
        for i in range(len(my_list)):
            for x in my_list[len(my_list)-i-1]:
                res.append(x)
                if len(res)==k:
                    return res
        
