class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):

            # skip over duplicate nums
            if i > 0 and num == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            while left < right: 
                current_sum = num + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # if three nums = 0
                    result.append([num, nums[left], nums[right]])
                    left += 1

                    # skips over duplicate values
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
        
        return result

