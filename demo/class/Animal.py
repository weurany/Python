class Animal(object):
	def __init__(self, name):
		self.name = name
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print '%s is running...' % self.name
	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	def run(self):
		print '%s is running...' % self.name 
	def eat(self):
		print 'Eating fish...'

dog = Dog('aa')
cat = Cat('bb')
dog.run()
dog.eat()
cat.run()
cat.eat()

