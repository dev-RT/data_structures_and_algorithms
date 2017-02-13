#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python Queue implementation
'''

class Empty(Exception):
    '''Custom Exception Class'''
    pass

class ArrayQueue(object):
    '''FIFO Queue implementation using a Python list as underlying storage.'''
    DEFAULT_CAPACITY = 10

    def __init__(self):
        '''Create an empty queue.
        '''
        self._front = 0
        self._size = 0
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY

    def __len__(self):
        '''Return the number of elements in the queue.
        '''
        return self._size

    def is_empty(self):
        '''Return True if the queue is empty.
        '''
        return self._size == 0

    def first(self):
        '''Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''Remove and return the first element of the queue (i.e. FIFO)
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, elem):
        '''Add an element to the back of the queue.
        '''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elem
        self._size += 1

    def _resize(self, cap):
        '''Resize to a new list of capacity >= len(self)
        '''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def display(self):
        '''Display queue elements'''
        print self._data[self._front: ((self._front + self._size) % len(self._data))]

if __name__ == '__main__':
    QUEUE_INSTANCE = ArrayQueue()
    QUEUE_INSTANCE.enqueue(5) #Add an element to the back of the queue.
    QUEUE_INSTANCE.enqueue(55) #Add an element to the back of the queue.
    QUEUE_INSTANCE.enqueue(555) #Add an element to the back of the queue.
    QUEUE_INSTANCE.display() #Display the elements of the queue.
    print len(QUEUE_INSTANCE) #Print number of elements in the queue.
    QUEUE_INSTANCE.dequeue() #Remove and return the first element of the queue
    QUEUE_INSTANCE.dequeue() #Remove and return the first element of the queue
    QUEUE_INSTANCE.display() #Display the elements of the queue.
    print QUEUE_INSTANCE.is_empty() #Return True if the queue is empty.
    QUEUE_INSTANCE.dequeue() #Remove and return the first element of the queue
    QUEUE_INSTANCE.display() #Display the elements of the queue.
    QUEUE_INSTANCE.enqueue(9) #Add an element to the back of the queue.
    QUEUE_INSTANCE.display() #Display the elements of the queue.
