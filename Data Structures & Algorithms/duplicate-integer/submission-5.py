class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute Force
        # O(n^2) complexity
        # O(n) space
        for i in range(len(nums)):       # O(n)
            for j in range(len(nums)):   # O(n)
                if i!=j and nums[i] == nums[j]:
                    return True
        return False
                    