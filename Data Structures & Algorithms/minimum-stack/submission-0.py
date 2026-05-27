class MinStack:

    def __init__(self):
        # Main stack stores all values
        self.stack = []

        # Min stack stores the minimum value
        # at each level of the stack
        self.minStack = []

    def push(self, val: int) -> None:
        # Add value to main stack
        self.stack.append(val)

        # If minStack is not empty,
        # compare current value with current minimum
        # and keep the smaller one
        val = min(val, self.minStack[-1] if self.minStack else val)

        # Store the current minimum
        self.minStack.append(val)

    def pop(self) -> None:
        # Remove top element from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return top value from main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return current minimum value
        return self.minStack[-1]