#!/usr/bin/env python

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        print _private_1(name)
    else:
        print _private_2(name)

if __name__ == '__main__':
	greeting('weihuan')
