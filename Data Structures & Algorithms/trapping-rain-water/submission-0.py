class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_l, max_r = height[left], height[right]

        s = 0
        # time O(n), space O(1)
        while left < right:
            h =  min(max_l, max_r)
            if max_l < max_r:
                s += h - height[left]
                left += 1
                max_l = max(max_l, height[left])
            else:
                s += h - height[right]
                right -= 1
                max_r = max(max_r, height[right])
        
        return s