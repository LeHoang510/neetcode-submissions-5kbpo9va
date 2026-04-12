class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # basic
        max_l = 0
        my_set = set(nums)
        for i, n in enumerate(nums):
            x = n + 1
            l = 1
            while x in my_set:
                l+=1
                x+=1
            if l>max_l:
                max_l=l
        return max_l
