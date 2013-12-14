#!/usr/bin/env python3

# Implement a MyQueue class which implements a queue using two stacks.

#-------------------------------------------------------

class MyQueue:

    """A queue class which follows the FIFO (First In, First Out) principle."""

    def __init__(self):

        # Init two empty stacks, which will be used internally to implement the
        # queue. These two stacks support push() and pop(), and follow the
        # standard FILO (First In, Last Out) stack principle
        self._main = list()
        self._temp = list()

    def push(self, value):
        "Take a value and push it into the queue."

        # Push to the main stack
        self._main.append(value)

    def pop(self):
        """Pop and return the oldest value in the queue."""

        # Pop all but first element in the main stack, and push them to the
        # temp stack. The remaining element is the oldest in the stack, and is
        # what we will return.
        while len(self._main) > 1:
            self._temp.append(self._main.pop())

        # Remember the last remaining value in the main stack so we can return
        # it.
        ret_value = self._main.pop()

        # Main stack is now empty. Pop all the values from the temp stack and
        # push back into the main stack. They remain in the correct order so we
        # can repeat these steps next time the user wants to pop from the queue
        while len(self._temp) > 0:
            self._main.append(self._temp.pop())

        # Return the value
        return ret_value

#-------------------------------------------------------

queue = MyQueue()

for num in range(5):
    queue.push(num)

assert queue.pop() == 0
assert queue.pop() == 1
assert queue.pop() == 2

queue.push(29)
queue.push(14)

assert queue.pop() == 3
assert queue.pop() == 4
assert queue.pop() == 29
assert queue.pop() == 14

queue.push("applesauce")
queue.push(123)

assert queue.pop() == "applesauce"

queue.push([3,5,7])

assert queue.pop() == 123
assert queue.pop() == [3,5,7]
