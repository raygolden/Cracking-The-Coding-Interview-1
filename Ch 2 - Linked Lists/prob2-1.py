#!/usr/bin/env python3

# Write code to remove duplicates from an unsorted
# linked list. How would you solve this problem if
# a temporary buffer isn't allowed?

from LinkedList import SinglyLinkedNode as Node
from LinkedList import get_singly_linked_list_from_values, count_nodes
import random

#-------------------------------------------------------

def remove_duplicates(head):

	pointer1 = head

	pointer2 = head.next
	previous = pointer1

	while pointer1 is not None:

		pointer2 = pointer1.next
		previous = pointer1

		while pointer2 is not None:
			if pointer2.data == pointer1.data:
				previous.next = pointer2.next

			previous = pointer2
			pointer2 = pointer2.next

		pointer1 = pointer1.next

#-------------------------------------------------------

for _ in range(10):

	# make the size of this linked list somewhere between
	# 5 and 30
	size = random.randint(5,31)

	# create a list of "size" number of integers and then
	# add the integers 0-4 to it again as duplicate data
	ll_values = list(range(size))
	ll_values.extend(list(range(5)))

	# shuffle the list so it's in random order
	random.shuffle(ll_values)

	head = get_singly_linked_list_from_values(ll_values)

	# at this point remove the duplicates
	remove_duplicates(head)

	# the count (number of nodes) of the linked list should
	# be equal to "size" defined above, since duplicates should
	# be removed
	assert count_nodes(head) == size
