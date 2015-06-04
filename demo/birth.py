# -*- coding: utf-8 -*-

birth = 00
while birth >= 0:
	birth = int(raw_input('birth : '))
	if birth > 2000:
		print '00后'
	elif birth < 2000 and birth > 0: 
		print '00前'
	elif birth < 0:
		print '退出'
