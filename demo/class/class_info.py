print 'type(123) is %s' % type(123)
print 'type(\'str\') is %s' % type('str')
print 'type(None) is %s' % type(None)
print 'type([]) is %s' % type([])
print 'type(u\'abc\') is %s' % type(u'abc')
print 'type(int)==type(str) is %s' % type(int)

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
	def __len__(self):
		return 100
obj = MyObject()
print 'len(obj) is %s' % len(obj)
print 'hasattr(obj, \'x\') is %s' % hasattr(obj, 'x')
print 'hasattr(obj, \'y\') is %s' % hasattr(obj, 'y')
print 'set attr y = 10'
setattr(obj, 'y', 10)
print 'hasattr(obj, \'y\') is %s' % hasattr(obj, 'y')
print 'getattr(obj, \'y\') is %s' % getattr(obj, 'y')

fn = getattr(obj, 'power')
print 'fn() is %d' % fn()

print dir(obj)

