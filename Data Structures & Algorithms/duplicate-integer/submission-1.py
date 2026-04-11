class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums) # o(n) space and time
        return not (len(my_set)==len(nums))