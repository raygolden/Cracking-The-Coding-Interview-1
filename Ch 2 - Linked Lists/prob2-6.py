#!/usr/bin/env python3

# Given a circular linked list, implement an algorithm which returns
# the node at the beginning of the loop.
#
# Circular linked list: A (corrupt) linked list in which a node’s next
# pointer points to an earlier node, so as to make a loop in the linked list.
#
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

from LinkedList import SinglyLinkedNode as Node
from LinkedList import get_singly_linked_list_from_values
import random

#-------------------------------------------------------

def find_linked_list_loop_start(head):

    all_nodes = list()

    current = head
    all_nodes.append(current)

    while True:
        current = current.next

        if current not in all_nodes:
            all_nodes.append(current)

        else:
            return current

#-------------------------------------------------------

a, b, c = Node(1), Node(2), Node(3)
a.next, b.next, c.next = b, c, b

assert find_linked_list_loop_start(a) is b

a, b, c, d, e = Node(1), Node(2), Node(3), Node(4), Node(5)

a.next, b.next, c.next = b, c, d
d.next, e.next = e, c

assert find_linked_list_loop_start(a) is c
