from .SinglyLinkedNode import SinglyLinkedNode
from .DoublyLinkedNode import DoublyLinkedNode


def get_singly_linked_list_from_values(value_list):

    head = SinglyLinkedNode(value_list[0])
    current = head

    for value in value_list[1:]:
        new_node = SinglyLinkedNode(value)
        current.next = new_node
        current = new_node

    return head


def get_doubly_linked_list_from_values(value_list):

    head = DoublyLinkedNode(value_list[0])
    current = head
    previous = None

    for value in value_list[1:]:
        new_node = DoublyLinkedNode(value)

        current.next = new_node
        new_node.last = current

        current = new_node

    return head


def count_nodes(head):

    count = 0

    current = head
    while current.next is not None:
        count += 1
        current = current.next

    count += 1

    return count


def linked_lists_equal(head_1, head_2):

    if count_nodes(head_1) != count_nodes(head_2):
        return False

    current_1, current_2 = head_1, head_2
    if current_1.data != current_2.data:
            return False

    while current_1.next is not None and current_2.next is not None:

        current_1, current_2 = current_1.next, current_2.next
        if current_1.data != current_2.data:
            return False

    return True
