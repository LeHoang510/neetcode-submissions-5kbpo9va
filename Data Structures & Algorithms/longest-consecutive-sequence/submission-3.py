class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution
        my_set = set(nums)  # space O(n)
        max_l = 0

        # O(n) because iterate through n max 
        for n in nums:
            l = 1
            start = n
            if n-1 in my_set:
                continue
            else:
                while start+1 in my_set:
                    l += 1
                    start += 1
                max_l = max(max_l, l)
        
        return max_l
        
