class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # basic
        product = 1
        counter = 0
        for i in nums:
            if i != 0:
                product *= i
            else:
                counter += 1
        if counter >= 2:
            product = 0
        res = [product for _ in range(len(nums))]
        print(res)
        for i, v in enumerate(nums):
            if v != 0 and counter >= 1:
                res[i] = 0
            elif v != 0:
                res[i] = int(res[i]/v)
            
        return res