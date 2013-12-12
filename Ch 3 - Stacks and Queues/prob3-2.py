#!/usr/bin/env python3

# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop, and min
# should all operate in O(1) time.

#-------------------------------------------------------

class EnhancedStack:
    """A stack with all the normal operations (push, pop) available, and also
    a min function which returns the minimum element currently in the stack."""

    def __init__(self, initial_size=50):

        self._data = [None for _ in range(initial_size)]
        self._min_stack = list()

    def __grow__(self):
        """Double the current size of the internal array, since the current
        size is no longer sufficient."""

        self._data.extend(None for _ in range(len(self._data)))

    def push(self, value):
        """Push a value onto the stack."""

        # If this is the first item, or if it's less than the current minimum,
        # add it to the min stack
        if len(self._min_stack) == 0 or value < self._min_stack[-1]:
            self._min_stack.append(value)

        # Check if there's room before we try to push. If not, grow.
        if None not in self._data:
            self._grow()

        first_open_index = self._data.index(None)
        self._data[first_open_index] = value

    def pop(self):
        """Pop a value from the stack and return it."""

        first_open_index = None

        if None not in self._data:
            first_open_index = len(self._data)
        else:
            first_open_index = self._data.index(None)

        # The last occupied index will be immediately before the first
        # open one. Get the value out if it and store it.
        last_occupied_index = first_open_index - 1
        ret_value = self._data[last_occupied_index]

        # Now that we have the last value stored, set that element to None.
        self._data[last_occupied_index] = None

        # Check to see if the element we're about to return is the minimum.
        # If so, pop it from the min stack to update the minimum.
        if ret_value == self.min():
            self._min_stack.pop()

        return ret_value

    def min(self):
        """Get the minimum element currently in the stack."""

        return self._min_stack[-1]

#-------------------------------------------------------

stack = EnhancedStack()

for num in range(20):
    stack.push(num)

assert stack.min() == 0

for _ in range(10):
    stack.pop()

stack.push(-1)

assert stack.min() == -1

stack.pop()

assert stack.min() == 0
