class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sorting
        # time O(nlogn)
        # save in dict
        nums = [(key, val) for val, key in enumerate(nums)] # space O(n)
        nums = sorted(nums)     # O(nlogn)
        left, right = 0, len(nums)-1
        while left < right:
            total = nums[left][0]+nums[right][0]
            if total == target:
                return [min(nums[left][1], nums[right][1]), max(nums[left][1], nums[right][1])]
            if total>target:
                right-=1
            else:
                left+=1
        
    