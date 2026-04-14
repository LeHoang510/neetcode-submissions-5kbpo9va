class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        left, right = 0, len(heights)-1

        while left < right:
            l_h = heights[left]
            r_h = heights[right]
            a = (right-left)*min(r_h, l_h)
            max_a = max(a, max_a)

            if l_h<r_h:
                left+=1
            else:
                right-=1

        return max_a