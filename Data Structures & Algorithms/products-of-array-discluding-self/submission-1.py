class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # without division

        l = len(nums)
        res = [1 for _ in range(l)]

        # product of the right
        right = 1
        for i in range(l-1, -1, -1):
            res[i] = right
            right *= nums[i]
        print(res)
        
        left = 1
        # product of the left
        for i in range(l):
            res[i] *= left
            left *= nums[i]
        print(res)
        
            
        return res