#!/usr/bin/env python3

# Implement a function void reverse(char* str) in C or C++ which
# reverses a null-terminated string

# Let's just do it in Python for kicks. And we'll have to return the
# reversed string since Python strings are immutable.

#-------------------------------------------------------

def my_reverse(string):
	new_str = list()

	# iterate through 'string' in reverse using -1 step slices
	for char in string[::-1]:
		new_str.append(char)

	return "".join(new_str)

#-------------------------------------------------------

strings_to_test = ["hello", "Hello", "12321123455432141", "#$@#$&.asdb#$2. "]

for string in strings_to_test:
	assert my_reverse(string) == "".join(reversed(string))

