#!/usr/bin/env python3

# Given two strings, write a method to decide if one is
# a permutation of the other

#-------------------------------------------------------

def get_char_frequency(string):
	""" Return a character frequency dictionary for the
	given string. The keys are the characters, the values
	are the number of instances of that character."""

	char_dict = dict()

	for char in string:
		if char in char_dict.keys():
			char_dict[char] += 1
		else:
			char_dict[char] = 1

	return char_dict

def are_permutations(first, second):
	""" Returns whether the two given string are are_permutations
	of each other."""

	first_dict = get_char_frequency(first)
	second_dict = get_char_frequency(second)

	# if the character frequency dicts are the same, the strings
	# are permutations of each other
	return first_dict == second_dict

#-------------------------------------------------------

assert are_permutations("abcdefg", "bgcdaef")
assert are_permutations("apple sauce", " suacepplae")

assert are_permutations("aaa b c", "bc aaa") is False
assert are_permutations("python", "ruby") is False