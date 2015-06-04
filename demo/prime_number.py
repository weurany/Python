import math
def ifsushu(a):
	i=2
	while (i <= int(math.sqrt(a))):
		if a%i == 0:
			return True
		i=i+1
	return False
print filter(ifsushu,range(101)[1:101])
