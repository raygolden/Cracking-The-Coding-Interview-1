#!/usr/bin/env python3

# Write an algorithm such that if an element in a MxN
# matrix is 0, its entire row and column are set to 0

import copy

#-------------------------------------------------------

def expand_zero_to_row_column(matrix):

	matrix_copy = copy.deepcopy(matrix)

	num_rows = len(matrix)
	num_cols = len(matrix[0])

	for row_index in range(num_rows):
		for col_index in range(num_cols):

			if matrix[row_index][col_index] == 0:
				for row in range(num_rows):
					matrix_copy[row][col_index] = 0
				for col in range(num_cols):
					matrix_copy[row_index][col] = 0

	return matrix_copy

#-------------------------------------------------------

origin_matrix = [[1,2,3],
      		     [4,0,5],
          		 [6,7,8]]

zeroed_matrix = [[1,0,3],
                 [0,0,0],
                 [6,0,8]]

assert expand_zero_to_row_column(origin_matrix) == zeroed_matrix

origin_matrix = [[1,0],
                 [1,1],
                 [1,1],
                 [1,1],
                 [1,1]]

zeroed_matrix = [[0,0],
                 [1,0],
                 [1,0],
                 [1,0],
                 [1,0]]

assert expand_zero_to_row_column(origin_matrix) == zeroed_matrix

origin_matrix = [[1,0,1,1],
				 [1,1,1,1],
				 [1,1,1,0]]

zeroed_matrix = [[0,0,0,0],
				 [1,0,1,0],
				 [0,0,0,0]]

assert expand_zero_to_row_column(origin_matrix) == zeroed_matrix