''' Write a Python class that simulates a Queue.
The class should implement methods like push, pop, peek
(the last two methods should return None if no element is present in the queue).'''


class Queue:
    def __init__(self):
        self.queue = []

    def get_queue(self):
        return self.queue

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
        return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None
