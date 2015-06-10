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
class bird(animal):
	def iswhat(self):
		print '%s is bird' % self.name
class runable(action):
	def run(self):
		print '%s can run' % self.name
class dog(animal, runable):
	def iswhat(self):
		print '%s is a dog' % self.name 

a = dog('Tom')
a.run()
a.iswhat()

