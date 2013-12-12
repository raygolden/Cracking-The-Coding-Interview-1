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
    """Return the top of the stack if it exists, or the largest
    possible integer if it does not."""

    try:
        return tower[-1]
    except:
        return sys.maxsize


def legal_disk_move(tower_1, tower_2):
    """Given two towers, perform the only legal disk move available."""

    if peek(tower_1) < peek(tower_2):
        tower_2.append(tower_1.pop())
    else:
        tower_1.append(tower_2.pop())


def print_tower_states(first, middle, last):
    """Convenience utility which prints the current states of all towers."""

    print()
    for tower in (first, middle, last):
        print(tower)


def assert_towers_valid(first, middle, last):
    """Asserts that each tower only has disks in ascending order of size
    from top to bottom."""

    assert first == sorted(first, reverse=True)
    assert middle == sorted(middle, reverse=True)
    assert last == sorted(last, reverse=True)

#-------------------------------------------------------

# Create towers
start_tower = list()
middle_tower = list()
target_tower = list()

# Let's play Towers of Hanoi with these numbers of disks
disk_nums_to_try = [1, 2, 5, 7, 8, 13, 20]

# Play each Tower of Hanoi game with N disks
for N in disk_nums_to_try:

    # Clear previous tower states and then push disks to the starting tower
    for tower in (start_tower, middle_tower, target_tower):
        tower.clear()

    start_tower.extend(range(N, 0, -1))

    # Using the iterative algorithm described in Wikipedia's Towers of Hanoi
    # page, we have to move disks between pairs of towers, in a certain order,
    # until the game is complete. The order of the pairs of towers is
    # dependant on whether N is even or odd
    if N % 2 == 0:
        ordered_tower_move_pairs = ((start_tower, middle_tower),
                                    (start_tower, target_tower),
                                    (middle_tower, target_tower))

    else:
        ordered_tower_move_pairs = ((start_tower, target_tower),
                                    (start_tower, middle_tower),
                                    (middle_tower, target_tower))

    # Swap disks between pairs of tairs, in order, until the final tower has
    # all of the disks
    while len(target_tower) < N:

        for tower_1, tower_2 in ordered_tower_move_pairs:

            # Actually perform the disk move
            legal_disk_move(tower_1, tower_2)

            # Assert towers are actually valid after each move
            # (valid means disks are only on top of a larger disk)
            assert_towers_valid(start_tower, middle_tower, target_tower)

            # Break out of the for loop if we're done. If we don't, we might
            # try to pop from an empty tower
            if len(target_tower) == N:
                break

    print("Successfully completed {}-tower Towers of Hanoi.".format(N))
