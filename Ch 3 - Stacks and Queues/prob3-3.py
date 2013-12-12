#!/usr/bin/env python3

# Imagine a (literal) stack of plates. If the stack gets too high, it
# might topple. Therefore, in real life, we would likely start a new stack
# when the previous stack exceeds some threshold. Implement a data
# structure SetOfStacks that mimics this. SetOfStacks should be composed
# of several stacks and should create a new stack once the previous one
# exceeds capacity. SetOfStacks.push() and .pop() should behave
# identically to a single stack (that is, pop() should return the same
# values as it would if it were just a single stack).
#
# FOLLOW UP
#
# Implement a function popAt(int index) which performs a pop operation
# on a specific sub-stack.

#-------------------------------------------------------

class SetOfStacks:

    """A stack which internally maintains individual sub-stacks that remain
    less than a certain threshold in size. Behaves like a regular stack from
    an outside point-of-view."""

    def __init__(self, threshold=5):

        self._threshold = threshold
        self._stacks = [[]]

    def push(self, value):
        """Push a value onto the stack."""

        # Check that the most recent sub-stack hasn't yet reached the size
        # threshold. If it has, make a new sub-stack.
        if len(self._stacks[-1]) >= self._threshold:
            self._stacks.append([])

        # Get the most recent sub-stack and push to it.
        current_stack = self._stacks[-1]
        current_stack.append(value)

    def pop(self):
        """Pops and returns a value from the stack."""

        # Gets the most recent sub-stack, pops from it, and stores the value.
        current_stack = self._stacks[-1]
        ret_value = current_stack.pop()

        # If that pop caused the sub-stack to become empty, remove it from
        # the list of sub-stacks so we don't try to pop from it again.
        if len(current_stack) == 0:
            self._stacks.pop()

        return ret_value

    def pop_at(self, index):
        """Pops and returns a value from a specific sub-stack."""

        # Get the specific sub-stack the user wants, pop from it,
        # and store the value.
        current_stack = self._stacks[index]
        ret_value = current_stack.pop()

        # If that pop caused that sub-stack to become empty, remove it from the
        # list of sub-stacks so we can't try to pop from it again.
        if len(current_stack) == 0:
            self._stacks.pop(index)

        return ret_value

#-------------------------------------------------------

stacks = SetOfStacks()

print("\nSetOfStacks initial internal structure: {}".format(stacks._stacks))

print("\nAbout to push 12 values...")
for num in range(12):
    stacks.push(num)

print("\nSetOfStacks current internal structure: {}".format(stacks._stacks))

print("\nAbout to pop 4 values...")
for _ in range(4):
    stacks.pop()

print("\nSetOfStacks current internal structure: {}".format(stacks._stacks))

print("\nAbout to push 8 values...")
for num in range(8):
    stacks.push(num)

print("\nSetOfStacks current internal structure: {}".format(stacks._stacks))

print("\nAbout to pop 4 values from second sub-stack...")
for _ in range(4):
    stacks.pop_at(1)

print("\nSetOfStacks current internal structure: {}".format(stacks._stacks))

print("\nAbout to pop last value from second sub-stack...")
stacks.pop_at(1)

print("\nSetOfStacks current internal structure: {}".format(stacks._stacks))

print()
