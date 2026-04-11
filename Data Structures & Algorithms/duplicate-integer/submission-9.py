class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_list = set(nums)
        # o(n)
        return len(my_list) != len(nums)
        