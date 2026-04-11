class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in my_dict:
                return [my_dict[num], i]
            else:
                my_dict[target-num] = i
    