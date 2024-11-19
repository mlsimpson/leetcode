class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# oops, misread problem, MinStack only holds the minimum
# need to do all these in constant time
# e.g. min(self.stack) isn't constant time
# hint on problem implies 2 stacks:
# "Consider each node in the stack having a minimum value."

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        # self.stack.pop()
        self.stack = self.stack[:len(self.stack) - 1]
        # self.min_stack.pop()
        self.min_stack = self.min_stack[:len(self.min_stack) - 1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

