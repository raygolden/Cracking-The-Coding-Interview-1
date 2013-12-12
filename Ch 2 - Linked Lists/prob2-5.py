#!/usr/bin/env python3

# You have two numbers represented by a linked list, where each
# node contains a single digit. The digits are stored in reverse order,
# such that the 1’s digit is at the head of the list. Write a function
# that adds the two numbers and returns the sum as a linked list.
#
# EXAMPLE
# Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8

from LinkedList import get_singly_linked_list_from_values, linked_lists_equal
import random

#-------------------------------------------------------

def add_linked_list_numbers(head_num_one, head_num_two):

    numbers = list()

    for head in (head_num_one, head_num_two):

        current = head
        digits = list()

        while current.next is not None:
            digits.append(current.data)
            current = current.next

        digits.append(current.data)
        num = int(''.join(str(digit) for digit in reversed(digits)))

        numbers.append(num)

    number_sum_str = str(sum(numbers))
    reversed_digits = [int(digit) for digit in list(reversed(number_sum_str))]

    return get_singly_linked_list_from_values(reversed_digits)

#-------------------------------------------------------

num_1 = get_singly_linked_list_from_values([1,2,3])
num_2 = get_singly_linked_list_from_values([4,8,6])

desired_sum = get_singly_linked_list_from_values([5,0,0,1])
calculated_sum = add_linked_list_numbers(num_1, num_2)

assert linked_lists_equal(desired_sum, calculated_sum)


num_1 = get_singly_linked_list_from_values([1,1,1,0,1,7])
num_2 = get_singly_linked_list_from_values([2,3,4,0,9,4])

desired_sum = get_singly_linked_list_from_values([3,4,5,0,0,2,1])
calculated_sum = add_linked_list_numbers(num_1, num_2)

assert linked_lists_equal(desired_sum, calculated_sum)
