#!/usr/bin/env python3

# In the classic problem of the Towers of Hanoi, you have 3 towers and N
# disks of difference sizes which can slide onto any tower. The puzzle
# starts with the disks sorted is ascending order of size from top to
# bottom (ie.e, each disk sits on top of an even larger one). You have the
# following constraints:
#
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto the next tower.
# (3) A disk can only be placed on top of a larger disk.
#
# Write a program to move the disks from the first tower to the last using
# stacks.

import sys

#-------------------------------------------------------

def peek(tower):

    try:
        return tower[-1]

    except:
        return sys.maxsize

def print_tower_states(first, middle, last):

    print()

    for tower in (first, middle, last):
        print(tower)

#-------------------------------------------------------

# Number of disks in Towers of Hanoi game
N = 10
previous_move = None

start_tower = list()
for num in range(N,0,-1):
    start_tower.append(num)

middle_tower = list()
target_tower = list()

print_tower_states(start_tower, middle_tower, target_tower)

if N % 2 == 0:

    while len(target_tower) < N:

        if peek(middle_tower) < peek(start_tower):
            start_tower.append(middle_tower.pop())
        else:
            middle_tower.append(start_tower.pop())

        if peek(target_tower) < peek(start_tower):
            start_tower.append(target_tower.pop())
        else:
            target_tower.append(start_tower.pop())

        if peek(target_tower) < peek(middle_tower):
            middle_tower.append(target_tower.pop())
        else:
            target_tower.append(middle_tower.pop())

else:

    while len(target_tower) < N:

        if peek(target_tower) < peek(start_tower):
            start_tower.append(target_tower.pop())
        else:
            target_tower.append(start_tower.pop())

        if peek(middle_tower) < peek(start_tower):
            start_tower.append(middle_tower.pop())
        else:
            middle_tower.append(start_tower.pop())

        if peek(target_tower) < peek(middle_tower):
            middle_tower.append(target_tower.pop())
        else:
            target_tower.append(middle_tower.pop())

print_tower_states(start_tower, middle_tower, target_tower)
