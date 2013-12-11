#!/usr/bin/env python3

# Assume you have a method isSubstring which checks if one
# string is a substring of another. Given two strings s1 and s2,
# write code to check if s2 is a rotation of s1 using only one
# call to isSubstring. 

# e.g. "waterbottle" is a rotation of "erbottlewat"

#-------------------------------------------------------

def is_substring(s1, s2):
	"""Checks if s1 is a substring of s2"""

	return s1 in s2

def is_rotation(s1, s2):
	"""Checks if s2 is a rotation of s1"""

	return is_substring(s1, s2 + s2)

#-------------------------------------------------------

assert is_rotation("waterbottle", "erbottlewat")

assert is_rotation("er", "re")

assert is_rotation("The woodchuck chucks wood.", " woodchuck chucks wood.The")

assert is_rotation("abcde fgh ijkl mnop", " fgh ijkl mnopabcde")