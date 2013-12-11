#!/usr/bin/env python3

# Implement an algorithm to find the kth to last element
# of a singly linked list

from LinkedList import SinglyLinkedNode as Node
from LinkedList import get_singly_linked_list_from_values, count_nodes
import random

#-------------------------------------------------------

def get_kth_to_last(head, k):

	pointer1 = head

	while pointer1.next is not None:

		steps_to_end = 0
		pointer2 = pointer1

		while pointer2.next is not None:
			steps_to_end += 1
			pointer2 = pointer2.next

		if (steps_to_end) == k:
			return pointer1.next

		pointer1 = pointer1.next

#-------------------------------------------------------

for _ in range(100):

	size = random.randint(10,100)
	k = random.randint(1,size-1)

	vals = list(range(size))
	random.shuffle(vals)

	head = get_singly_linked_list_from_values(vals)

	assert get_kth_to_last(head, k).data == vals[-k]