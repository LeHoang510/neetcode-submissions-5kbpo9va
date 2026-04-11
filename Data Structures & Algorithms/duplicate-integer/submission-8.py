class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sorting
        # O(n) complexity
        # O(1) space
        nums = sorted(nums)             # O(nlogn) complexity
        for i in range(len(nums)-1):    # O(n) complexity
            if nums[i] == nums[i+1]:
                return True
        return False