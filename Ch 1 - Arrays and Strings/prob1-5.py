#!/usr/bin/env python3

# Implement a method to perform basic string compression using
# the counts of repeated characters. For example, the string
# 'aabcccccaaa' would become 'a2b1c5a3'. If the compressed string
# is longer than the original string, return the original string.

#-------------------------------------------------------

def char_count_compress(string):

	compressed = list()
	current_char = None
	current_count = 0

	for index in range(len(string)):
		if string[index] == current_char:
			current_count += 1
		else:
			if current_char is not None:
				compressed.append(current_char)
				compressed.append(str(current_count))

			current_count = 1
			current_char = string[index]

	compressed.append(current_char)
	compressed.append(str(current_count))

	compressed_string = "".join(compressed)

	if len(compressed_string) > len(string):
		return string
	else:
		return compressed_string

#-------------------------------------------------------

assert char_count_compress("aabcccccaaa") == "a2b1c5a3"
assert char_count_compress("aaaaaa bbbbbb") == "a6 1b6"
assert char_count_compress("abcde") == "abcde"