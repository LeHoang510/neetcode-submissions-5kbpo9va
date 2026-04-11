class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time O(n)
        # Space O(n)
        my_dict = {}                        # O(n)
        for i in range(len(nums)):          # O(n)
            num = nums[i]
            if num in my_dict:
                return [my_dict[num], i]
            else:
                my_dict[target-num] = i
    