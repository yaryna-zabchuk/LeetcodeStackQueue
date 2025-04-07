'''A queue implemented using a doubly linked list'''

class Node:
    '''A node in a doubly linked list.'''
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class Queue:
    '''A queue implemented using a doubly linked list.'''
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        '''Push a value to the back of the queue.'''
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def pop(self):
        '''Pop a value from the front of the queue.'''
        if not self.head:
            return None
        val = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def peek(self):
        '''Peek at the front value of the queue.'''
        if not self.head:
            return None
        return self.head.value

    def empty(self):
        '''Check if the queue is empty.'''
        return self.head is None
