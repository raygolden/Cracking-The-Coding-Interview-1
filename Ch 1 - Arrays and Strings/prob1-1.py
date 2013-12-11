#!/usr/bin/env python3

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

#-------------------------------------------------------

def test_for_only_unique(string):

	def additional_data_structures_ok():
		return len(string) == len(set(string))

	def additional_data_structures_not_ok():
		# Initialize a False-filled list of size 256, because we're assuming ascii.
		# Unicode solution would be the same, with an appropriately sized larger list
		char_set = [False] * 256

		for char in string:
			if char_set[ord(char)]:
				return False
			else:
				char_set[ord(char)] = True

		return True

	return additional_data_structures_ok, additional_data_structures_not_ok

#-------------------------------------------------------

duplicate_chars = "I have duplicate characters"
no_duplicate_chars = "I_have-no*dups"

test1, test2 = test_for_only_unique(duplicate_chars)
assert test1() is False
assert test2() is False

test1, test2 = test_for_only_unique(no_duplicate_chars)
assert test1()
assert test2()
