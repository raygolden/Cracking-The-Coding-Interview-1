#!/usr/bin/env python3

# Implement a function to determine if a linked list is a palindrome.

# Let's do it for singly linked lists, since doubly linked would be
# considerably easier.

from LinkedList import SinglyLinkedNode as Node
from LinkedList import get_singly_linked_list_from_values as get_list
from LinkedList import count_nodes
import random

#-------------------------------------------------------

def are_palindromes(head_1, head_2):

    if count_nodes(head_1) != count_nodes(head_2):
        return False

    # Find the tail of the second list to begin with
    current_two = head_2

    while current_two.next is not None:
        current_two = current_two.next

    tail_2 = current_two

    # Start comparing the first element of list one with the last element of
    # list two, and work inwards until we're done or they don't match.
    current_one, current_two = head_1, tail_2

    while current_one.next is not None:

        if current_one.data != current_two.data:
            return False

        current_one = current_one.next

        next_two = head_2
        while next_two.next is not current_two:
            next_two = next_two.next

        current_two = next_two

    return True

#-------------------------------------------------------

assert are_palindromes(get_list([0,1,2,3]), get_list([3,2,1,0]))

assert are_palindromes(get_list([0]), get_list([0]))

assert are_palindromes(get_list(["apple", "blueberry"]), get_list(["blueberry","apple"]))

assert are_palindromes(get_list([1,2,3]), get_list([4,3,2,1])) is False

assert are_palindromes(get_list([0,1,0,1]), get_list([0,1,0,1])) is False
