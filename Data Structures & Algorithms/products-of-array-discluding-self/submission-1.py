class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # create output list which is filled with 1s
        output = [1] * len(nums)

        # store left side products
        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # store right side products
        suffix = 1

        for i in range(len(nums) -1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
