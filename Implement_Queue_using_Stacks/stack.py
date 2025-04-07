'''Class for stack implementation using linked list.'''

class Node:
    '''Node class for stack implementation.'''
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    '''Stack class using linked list.'''
    def __init__(self, next=None):
        self.next = next
        self.top = None

    def is_empty(self):
        '''Checks if the stack is empty'''
        return self.top is None

    def push(self, val):
        '''Pushes a value onto the stack'''
        self.top = Node(val, self.top)

    def pop(self):
        '''Pops the top value from the stack'''
        if self.is_empty():
            raise ValueError("Stack is empty")
        val = self.top.item
        self.top = self.top.next
        return val

    def peek(self):
        '''Returns the top value of the stack without removing it'''
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.item
