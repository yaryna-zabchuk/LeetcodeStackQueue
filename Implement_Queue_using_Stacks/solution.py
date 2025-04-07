'''Solution for Leetcode problem 232: Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
'''
from stack import Stack

class MyQueue:
    '''Class to implement a queue using two stacks'''
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def push(self, x: int) -> None:
        '''Push element x to the back of queue'''
        self.right.push(x)

    def pop(self) -> int:
        '''Removes the element from the front of queue and returns it'''
        if self.left.is_empty():
            while not self.right.is_empty():
                self.left.push(self.right.pop())
            return self.left.pop()
        return self.left.pop()

    def peek(self) -> int:
        '''Get the front element'''
        if self.left.is_empty():
            while not self.right.is_empty():
                self.left.push(self.right.pop())
        return self.left.peek()

    def empty(self) -> bool:
        '''Returns whether the queue is empty'''
        return self.right.is_empty() and self.left.is_empty()
