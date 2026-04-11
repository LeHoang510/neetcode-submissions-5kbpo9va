class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # new way to do it
        # o(nlogn)
        nums = [(k, v) for v, k in enumerate(nums)]
        nums = sorted(nums)
        left, right = 0, len(nums)-1

        while left < right:
            s = nums[left][0] + nums[right][0]
            if s == target:
                return [min(nums[left][1], nums[right][1]),
                max(nums[left][1], nums[right][1])]
            elif s > target:
                right-=1
            else:
                left+=1