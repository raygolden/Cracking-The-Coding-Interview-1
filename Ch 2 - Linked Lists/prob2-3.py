#!/usr/bin/env python3

# Implement an algorithm to delete a node in the middle of
# a singly linked list, given on access to that node.
#
# EXAMPLE:
# Input: the node 'c' from the linked list a->b->c->d->e
# Result: nothing is returned, but the
#         new linked list looks like a->b->d->e

from LinkedList import get_singly_linked_list_from_values
import random

#-------------------------------------------------------

def remove_this_node(node):

    # TODO: any way to do this if 'node' is the last
    # node in the list? Python keeps objects alive if
    # there are still references to them in scope.
    # Setting node to None, or deleting it, only affects
    # this reference. The previous node's reference to this
    # one still exists, and therefore I can't remove the
    # last node in a singly linked list.

    if node.next is not None:
        next_node = node.next
        node.data = next_node.data
        node.next = next_node.next

    else:
        node = None

#-------------------------------------------------------

for _ in range(100):

    vals = list(range(10))
    random.shuffle(vals)

    head = get_singly_linked_list_from_values(vals)

    # pick a random node to remove
    # TODO: make this go up to 9, not 8, if I can
    # figure out a way remove the last node in a
    # singly linked list
    current = head
    for _ in range(random.randint(0,8)):
        current = current.next

    # remember the data we're about to remove,
    data_removed = current.data
    remove_this_node(current)

    # build list of remaining data in linked list
    ll_data = list()
    current = head
    ll_data.append(current.data)

    while current.next is not None:
        current = current.next
        ll_data.append(current.data)

    # remove the deleted note's data from the original vals list
    vals.remove(data_removed)

    assert vals == ll_data
