class Animal(object):
	def __init__(self, name):
		self.__name = name
	def run(self):
		print 'Animal is running...'
	def get_name(self):
		return self.__name

class Dog(Animal):
	def run(self):
		print '%s is running...' % self.get_name()
	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	def run(self):
		print '%s is running...' % self.get_name()
	def eat(self):
		print 'Eating fish...'

dog = Dog('aa')
cat = Cat('bb')
dog.run()
dog.eat()
cat.run()
cat.eat()

