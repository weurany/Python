a = ['adam', 'LISA', 'barT']
def toself(ch):
	return ch
def change(s):
	return map(toself,s)
a= map(change,a)
def First(number):
	for i,ch in enumerate(number):
		if i==0:
			number[i]=number[i].upper()
		else:
			number[i]=number[i].lower()
	return reduce(lambda x,y:x+y, number)

a = map(First,a)
print a
