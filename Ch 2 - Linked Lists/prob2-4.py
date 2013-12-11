#!/usr/bin/env python3

from LinkedList import get_singly_linked_list_from_values
import random

#-------------------------------------------------------

def partition_linked_list_around(value, list_head):

    first_half, second_half = list(), list()

    current = list_head

    if current.data < value:
        first_half.append(current.data)
    else:
        second_half.append(current.data)

    while current.next is not None:

        current = current.next

        if current.data < value:
            first_half.append(current.data)
        else:
            second_half.append(current.data)

    return get_singly_linked_list_from_values(first_half + second_half)

#-------------------------------------------------------

values = list(range(20))
random.shuffle(values)

head = get_singly_linked_list_from_values(values)

current = partition_linked_list_around(6, head)

while current.next is not None:

    print(current.data)
    current = current.next

print(current.data)
