class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = sorted(numbers)
        left, right = 0, len(nums)-1
        
        # O(n)
        while left < right:
            total = nums[left]+nums[right]
            if target == total:
                return [left+1, right+1]
            elif target < total:
                right-=1
            else:
                left+=1
