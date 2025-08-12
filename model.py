class Model:
	def __init__(self, first = 0 ,second = 0):
		self._first = first
		self._second = second
		self._answer = None
	@property
	def first(self):
		return self._first
	@first.setter
	def first(self,value):
		self._first = value
	@property
	def second(self):
		return self._second
	@second.setter
	def second(self,value):
		self._second = value
	def plus():
		self.answer = self._first + self._second
	def minus():
		self.answer = self._first - self._second
		
		
