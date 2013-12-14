#!/usr/bin/env python3

# Write a program to sort a stack in ascending order (with biggest items
# on top). You may use at most one additional stack to hold items, but you
# may not copy the elements into any other data structure (such as an
# array). The stack supports the following operations: push, pop, peek,
# and is_empty.

from random import shuffle
import sys

#-------------------------------------------------------

class Stack:

    def __init__(self):
        self._data = list()

    def push(self, value):
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

#-------------------------------------------------------

values = list(range(25))
shuffle(values)

stack_1, stack_2 = Stack(), Stack()

for value in values:
    stack_1.push(value)

print()
print(stack_1._data)
print(stack_2._data)

while not stack_1.is_empty():

    tmp = stack_1.pop()

    while not stack_2.is_empty() and stack_2.peek() > tmp:
        stack_1.push(stack_2.pop())

    stack_2.push(tmp)

print()
print(stack_1._data)
print(stack_2._data)
