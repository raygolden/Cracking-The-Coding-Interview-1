class DoublyLinkedNode(object):

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

