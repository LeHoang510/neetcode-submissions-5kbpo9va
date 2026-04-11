class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {} # space o(n)

        # time o(n)
        for i, val in enumerate(nums):
            res = target - val
            if val in my_dict.keys():
                return [my_dict[val], i]
            else:
                my_dict[res] = i