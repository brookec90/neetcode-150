class MinStack:

    def __init__(self):
        # empty list to store numbers
        self.stack = []
        # tracks current minimum
        self.min_stack = []

    def push(self, val: int) -> None:
        # add number to top of stack
        self.stack.append(val)

        # if min stack empty, add first number
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # compare new value w current min, stores smaller value
            smallest = min(val, self.min_stack[-1])
            self.min_stack.append(smallest)

    def pop(self) -> None:
        # remove top element from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # returns last element in list
        return self.stack[-1]
        
    def getMin(self) -> int:
        # return current min value
        return self.min_stack[-1]
