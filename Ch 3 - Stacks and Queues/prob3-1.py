#!/usr/bin/env python3

# Describe how you could use a single array to
# implement three stacks.

#-------------------------------------------------------

class TripleStack:

    """ An implementation of 3 stacks using a single array/list.
    Works for all types of data except None, which is used to denote
    an empty array/list entry in this implementation."""

    def __init__(self, initial_size=12):

        self._data = [None for _ in range(initial_size)]
        self._set_stack_pointers()

    def __len__(self):
        return len(self._data)

    def _grow(self):
        """Double the internal storage capacity of this TripleStack if
        the current capacity is not sufficient."""

        # For easy data handling later, get separate references to each
        # internal stack.
        stack0 = self._data[self._pointers[0]:self._pointers[1]]
        stack1 = self._data[self._pointers[1]:self._pointers[2]]
        stack2 = self._data[self._pointers[2]:self._pointers[3]]

        # Reset internal array to a list of None values twice its previous size.
        # Reset stack pointers so we know the new index ranges belonging to the
        # separate stacks
        self._data = [None for _ in range(len(self._data) * 2)]
        self._set_stack_pointers()

        # Fill data from first stack back into the array at the correct place.
        base_index = self._pointers[0]
        for i, value in enumerate(stack0):
            self._data[base_index + i] = value

        # Fill data from second stack back into the array at the correct place.
        base_index = self._pointers[1]
        for i, value in enumerate(stack1):
            self._data[base_index + i] = value

        # Fill data from third stack back into the array at the correct place.
        base_index = self._pointers[2]
        for i, value in enumerate(stack2):
            self._data[base_index + i] = value

    def _set_stack_pointers(self):
        """Update the set of 'pointer' values which internally help separate
        the values in the internal array into three logical stacks."""

        size = len(self._data)

        # The first three entries are indices of the start of stacks 0 - 2, and
        # the last is the index of the last element of the array.
        self._pointers = [0,
                          int(size / 3),
                          int(2 * size / 3),
                          size]

    def _push(self, which_stack, value):
        """Internal implementation of pushing a value into one of the three
        logical stacks."""

        # Slice internal array to get the logical stack we want to work on
        stack_start = self._pointers[which_stack]
        stack_end = self._pointers[which_stack + 1]
        stack = self._data[stack_start:stack_end]

        # Run this until we succeed in pushing to the stack
        while True:

            # Find the first 'empty' array element and stick the value there
            try:
                first_open_index = stack.index(None)
                self._data[stack_start + first_open_index] = value
                return

            # This should occur if stack.index(None) throws an exception,
            # meaning no None values exist, meaning the stack is currently
            # 'full' and we need to grow it.
            except Exception as e:
                self._grow()

                stack_start = self._pointers[which_stack]
                stack_end = self._pointers[which_stack + 1]

                stack = self._data[stack_start:stack_end]

    def _pop(self, which_stack):
        """Internal implementation of popping a value from one of the three
        internal stacks."""

        # Slice internal array to get the logical stack we want to work on
        stack_start = self._pointers[which_stack]
        stack_end = self._pointers[which_stack + 1]

        stack = self._data[stack_start:stack_end]

        # Find the last-occupied element in the stack, get the value, set that
        # element to None to indicate empty, and return its former value
        try:
            first_open_index = stack.index(None)
            last_occupied_index = stack_start + first_open_index - 1

            ret_value = self._data[last_occupied_index]
            self._data[last_occupied_index] = None

            return ret_value

        # Got here if stack.index(None) threw an exception, meaning no None
        # values, meaning the stack is full. Return the last element's value
        # after setting it to None
        except Exception as e:
            ret_value = self._data[stack_end - 1]
            self._data[stack_end - 1] = None

            return ret_value

    def push_to_first_stack(self, value):
        """Pushes value to the first stack."""
        self._push(0, value)

    def push_to_second_stack(self, value):
        """Pushes value to the second stack."""
        self._push(1, value)

    def push_to_third_stack(self, value):
        """Pushes value to the third stack."""
        self._push(2, value)

    def pop_from_first_stack(self):
        """Pop and return value from the first stack."""
        return self._pop(0)

    def pop_from_second_stack(self):
        """Pop and return value from the second stack."""
        return self._pop(1)

    def pop_from_third_stack(self):
        """Pop and return value from the third stack."""
        return self._pop(2)

#-------------------------------------------------------

tri_stack = TripleStack()

print("\nInitial TripleStack internal array length: {}".format(len(tri_stack)))
print("\nInitial state of TripleStack internal array:\n{}".format(tri_stack._data))

print("\nPushing 6 values to stack 1...")
for i in range(6):
    tri_stack.push_to_first_stack(i)

print("Pushing 6 values to stack 2...")
for i in range(7,13):
    tri_stack.push_to_second_stack(i)

print("Pushing 6 values to stack 3...")
for i in range(14,20):
    tri_stack.push_to_third_stack(i)

print("\nCurrent state of TripleStack internal array:\n{}".format(tri_stack._data))

print("\nPopping 3 values from stack 1...")
for _ in range(3):
    print("   {}".format(tri_stack.pop_from_first_stack()))

print("\nPopping 4 values from stack 2...")
for _ in range(4):
    print("   {}".format(tri_stack.pop_from_second_stack()))

print("\nPopping 5 values from stack 3...")
for _ in range(5):
    print("   {}".format(tri_stack.pop_from_third_stack()))

print("\nFinal TripleStack internal array length: {}".format(len(tri_stack)))
print("\nFinal state of TripleStack internal array:\n{}".format(tri_stack._data))
