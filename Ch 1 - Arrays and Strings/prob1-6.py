#!/usr/bin/env python3

# Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image
# by 90 degrees. Can you do this in place?

#-------------------------------------------------------

def rotate_90_using_zip(image):

	# reverse "rows" (inner lists) in original image list
	# unpack to tuples with *
	# zip matches up nth elements of each tuple into their own tuple
	# list turns the zip object into a list
	# we have a list of tuples now, which is the rotated image
	tupled_list = list(zip(*reversed(image)))

	# use list comprehension to turn list of tuples into
	# list of lists
	return [list(row) for row in tupled_list]

def rotate_90_no_help(image):

	reversed_rows = [list(row) for row in reversed(image)]
	row_length = len(reversed_rows[0])

	new_image = list()

	for index in range(row_length):
		new_row = list()

		for row in reversed_rows:
			new_row.append(row[index])

		new_image.append(new_row)

	return new_image

#-------------------------------------------------------

image = [[1,2],
		 [3,4]]

rot_image = [[3,1],
			 [4,2]]

assert rotate_90_using_zip(image) == rot_image
assert rotate_90_no_help(image) == rot_image

image = [[ 1, 2, 3, 4],
		 [ 5, 6, 7, 8],
		 [ 9,10,11,12],
		 [13,14,15,16]]

rot_image = [[13, 9, 5, 1],
             [14,10, 6, 2],
             [15,11, 7, 3],
             [16,12, 8, 4]]

assert rotate_90_using_zip(image) == rot_image
assert rotate_90_no_help(image) == rot_image

image = [[1,2,3,4,5],
         [6,7,8,9,0]]

rot_image = [[6,1],
             [7,2],
             [8,3],
             [9,4],
             [0,5]]

assert rotate_90_using_zip(image) == rot_image
assert rotate_90_no_help(image) == rot_image
