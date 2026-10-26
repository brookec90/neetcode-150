class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
        
            #calc areas when we come across a shorter bar
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_area = max(max_area, h * (i-index))

                #extend current rectangle to the left
                start = index
            
            #store earliest starting index & current height
            stack.append((start, height))
        
        #calc areas for bars remaining in stack
        for index, h in stack: 
            max_area = max(max_area, h * (len(heights) - index))
        
        return max_area
        
        