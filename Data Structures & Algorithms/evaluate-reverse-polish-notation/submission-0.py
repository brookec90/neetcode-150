class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        #process each token, using stack to evaluate operators
        for token in tokens:
            if token in ["+", "-", "*", "/"]:

                # pop operators in reverse order, relevant for - & /
                first = stack.pop()
                second = stack.pop()

                if token == "+":
                    result = first + second
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = first * second
                elif token == "/":
                    # truncate division towards zero
                    result = int(second/first)

                stack.append(result)

            else:
                # convert number tokens from strings to integers
                stack.append(int(token))
        
        return stack[0]
        