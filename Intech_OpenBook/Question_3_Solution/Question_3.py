class MinStack:
    def __init__(self):
        # Initialize the main stack and the min stack
        self.stack = []       # The main stack to store values
        self.min_stack = []   # The min stack to keep track of minimum values

    def push(self, value):
        # Add the value to the main stack
        self.stack.append(value)

        # If the min stack is empty or the value is less than or equal to the top value of the min stack,
        # add the value to the min stack to keep track of the minimum values
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        # Check if the main stack is empty
        if not self.stack:
            return None

        # Remove the top value from the main stack
        value = self.stack.pop()

        # If the popped value is the same as the top value of the min stack,
        # it means the minimum value has been removed, so remove it from the min stack as well
        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def min(self):
        # Check if the min stack is empty
        if not self.min_stack:
            return None

        # Return the top value of the min stack, which represents the minimum value in the stack
        return self.min_stack[-1]
