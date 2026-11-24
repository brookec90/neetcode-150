class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            # calc midpoint index
            mid = (left+right) // 2 

            # search right side
            if nums[mid] < target:
                left = mid + 1
            # search left side
            elif nums[mid] > target:
                right = mid - 1
            # when target found, return its index num
            else:
                return mid
                
        # if target not found
        return -1
            

        