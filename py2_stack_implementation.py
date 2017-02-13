#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python Stack implementation
'''

class Empty(Exception):
    '''Custom Exception Class'''
    pass

class ArrayStack(object):
    '''LIFO Stack implementation using a Python list as underlying storage.'''

    def __init__(self):
        '''Create an empty stack'''
        self._data = []

    def __len__(self):
        '''return the number of elements in the stack'''
        return len(self._data)

    def is_empty(self):
        '''Return True if the stack is empty'''
        return len(self._data) == 0

    def push(self, data):
        ''' Add element to the top of the stack'''
        self._data.append(data)

    def top(self):
        '''Return the element at the top of the stack
        Raise empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        '''Remove and return element from the top of the stack
        Raise empty exception is stack is empty
        '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def display(self):
        '''Display stack elements'''
        print self._data

if __name__ == '__main__':
    STACK_INSTANCE = ArrayStack()
    VAL1 = 5
    VAL2 = 55
    VAL3 = 'some_test_string'
    print "Pushing '{}' on stack ".format(VAL1)
    STACK_INSTANCE.push(VAL1)
    print "Pushing '{}' on stack ".format(VAL2)
    STACK_INSTANCE.push(VAL2)
    print "Pushing '{}' on stack ".format(VAL3)
    STACK_INSTANCE.push(VAL3)
    print "Current stack is:",
    STACK_INSTANCE.display()
    print "Number of elements on stack: {}".format(len(STACK_INSTANCE))
    print "Is stack empty:", STACK_INSTANCE.is_empty()
    print "Popping out from stack:", STACK_INSTANCE.top()
    STACK_INSTANCE.pop()
    print "Popping out from stack:", STACK_INSTANCE.top()
    STACK_INSTANCE.pop()
    print "Is stack empty:", STACK_INSTANCE.is_empty()
    print "Current stack is:",
    STACK_INSTANCE.display()
    print "Popping out from stack:", STACK_INSTANCE.top()
    STACK_INSTANCE.pop()
    print "Current stack is:",
    STACK_INSTANCE.display()
    print "Is stack empty:", STACK_INSTANCE.is_empty()
