#!/usr/bin/env python3

# Write a method to replace all spaces in a string with "%20".
# You may assume that the string has sufficient space at the
# end of the string to hold the additional characters, and that
# you are given the 'true' length of the string.
#
# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# I think this problem doesn't really apply well to Python,
# since strings are immutable, and therefore you can't modify
# them in place. No need to know the 'true length' of the
# incoming string in that case, either.

#-------------------------------------------------------

def percent_20(string, true_length):

	new_str = list()

	for index in range(true_length):
		if string[index] == ' ':
			new_str.append("%20")
		else:
			new_str.append(string[index])

	return ''.join(new_str)

#-------------------------------------------------------

assert percent_20("Mr John Smith    ", 13) == "Mr John Smith".replace(' ', "%20")
assert percent_20("Hullaballoo", 11) == "Hullaballoo".replace(' ', "%20")
assert percent_20("                                ", 8) == "        ".replace(' ', "%20")