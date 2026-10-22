class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        # loop through temperatures w their day indices
        for i, temp in enumerate(temperatures):

            # resolve prev days when a warmer temp is found
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day

            # store current day index for future comparison
            stack.append(i)

        return result
        