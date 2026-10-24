class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # match car position with speed
        cars = list(zip(position, speed))

        #process cars from closest > furthest from target
        cars = sorted(cars, reverse=True)

        for pos, spd in cars:
            #calculate car arrival time
            time = (target- pos) / spd
            stack.append(time)

            #merge with fleet ahead if car catches up
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        #every stack entry is equivalent to one fleet
        return len(stack)