#!/usr/bin/env python3

# An animal shelter holds only dogs and cats, and operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they can
# select whether they would prefer a dog or a cat (and will receive the
# oldest animal of that type). They cannot select which specific animal
# they would like. Create the data structures to maintain this system and
# implement operations such as enqueue, dequeueAny, dequeueDog and
# dequeueCat. You may use the built-in LinkedList data structure.

#-------------------------------------------------------

class DoublyLinkedNode:

    def __init__(self, data):
        self._data = data
        self._next = None
        self._last = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        self._last = value

#-------------------------------------------------------

class AnimalQueue:

    def __init__(self):

        self._dog_queue = list()
        self._cat_queue = list()

        self._head = None

    def _enqueue(self, name, which_queue):

        new_node = DoublyLinkedNode(name)
        which_queue.append(new_node)

        if self._head is None:
            self._head = new_node

        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
            new_node.last = current_node

    def _dequeue(self, which_queue):

        animal_node = which_queue.pop(0)

        if animal_node is self._head:
            self._head = self._head.next

            if self._head is not None:
                self._head.last = None

        else:
            if animal_node.last is not None:
                animal_node.last.next = animal_node.next

            if animal_node.next is not None:
                animal_node.next.last = animal_node.last

        return animal_node.data

    def dequeueAny(self):

        if not len(self._dog_queue) == 0 and self._dog_queue[0] == self._head:
            return self.dequeueDog()

        else:
            return self.dequeueCat()

    def enqueueCat(self, name):

        self._enqueue(name, self._cat_queue)

    def enqueueDog(self, name):

        self._enqueue(name, self._dog_queue)

    def dequeueDog(self):

        return self._dequeue(self._dog_queue)

    def dequeueCat(self):

        return self._dequeue(self._cat_queue)

#-------------------------------------------------------

queue = AnimalQueue()

for cat in ('Whiskers', 'Fluffy', 'Mittens'):
    queue.enqueueCat(cat)

for dog in ('Fido', 'Rusty', 'Spot'):
    queue.enqueueDog(dog)

queue.enqueueCat('Ruby')
queue.enqueueDog('Rocko')

assert queue.dequeueAny() == 'Whiskers'
assert queue.dequeueDog() == 'Fido'
assert queue.dequeueDog() == 'Rusty'
assert queue.dequeueAny() == 'Fluffy'
assert queue.dequeueAny() == 'Mittens'
assert queue.dequeueCat() == 'Ruby'
assert queue.dequeueAny() == 'Spot'
assert queue.dequeueDog() == 'Rocko'

queue.enqueueCat('Meow Mix')
queue.enqueueDog('Pluto')

assert queue.dequeueDog() == 'Pluto'
assert queue.dequeueAny() == 'Meow Mix'
