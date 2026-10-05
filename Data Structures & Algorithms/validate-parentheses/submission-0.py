class Solution:
    def isValid(self, s: str) -> bool:
        
        #empty stack
        stack = []

        #store matching brackets
        matching = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            # check if char is a closing bracket
            if char in matching:
                if stack and stack[-1] == matching[char]:
                    # remove matching bracket
                    stack.pop()
                else:
                    return False
            # add opening bracket to matching
            else:
                stack.append(char)
        
        # stack will be empty when finished
        return len(stack) == 0