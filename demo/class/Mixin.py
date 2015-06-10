class origin_class(object):
	def __init__(self, name):
		self.name = name 
class animal(origin_class):
	def iswhat(self):
		print '%s is animal' % self.name
class action(origin_class):
	def iswhat(self):
		print '%s is action' % self.name
class mammal(animal):
	def iswhat(self):
		print '%s is mammal' % self.name
	def move(self):
		print '%s can move' % self.name
class bird(animal):
	def iswhat(self):
		print '%s is bird' % self.name
	def move(self):
		print '%s can move' % self.name
class runable(action):
	def iswhat(self):
		print '%s is something can run' % self.name 
	def move(self):
		print '%s can run' % self.name
class dog1(mammal, runable):
	pass
class dog2(runable, mammal):
	pass
a = dog1('dog1')
b = dog2('dog2')
a.move()
a.iswhat()
b.move()
b.iswhat()
