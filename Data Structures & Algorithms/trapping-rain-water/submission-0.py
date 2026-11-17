class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        # track tallest containers at each side
        leftMax = height[left]
        rightMax = height[right]
        # track total water collected
        water = 0

        while left < right:
            # process smaller side
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
            
        return water


        