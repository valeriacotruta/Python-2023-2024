'''Write a Python class that simulates a Stack. The class should implement methods like push,
pop, peek (the last two methods should return None if no element is present in the stack).'''


class Stack:
    def __init__(self):
        self.stack = []

    def get_stack(self):
        return self.stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop(len(self.stack) - 1)
        return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return None
