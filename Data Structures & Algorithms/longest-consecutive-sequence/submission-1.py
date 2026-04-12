class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # basic
        max_l = 0
        my_set = set(nums)              # space O(n)
        for i, n in enumerate(nums):    # time O(n)
            x = n + 1
            l = 1
            while x in my_set:          # time O(n)
                l+=1
                x+=1
            if l>max_l:                 # time O(1)
                max_l=l

        # time O(n2)
        return max_l
