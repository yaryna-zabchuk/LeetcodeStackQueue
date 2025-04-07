'''Solution for LeetCode problem 225: Implement Stack using Queues.
https://leetcode.com/problems/implement-stack-using-queues/submissions/1599751706/
'''
from queue import Queue

class MyStack:
    '''A stack implemented using two queues.'''
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, val):
        '''Push a value onto the stack.'''
        self.q2.push(val)
        while not self.q1.empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        '''Pop the top value off the stack.'''
        return self.q1.pop()

    def top(self):
        '''Peek at the top value of the stack.'''
        return self.q1.peek()

    def empty(self):
        '''Check if the stack is empty.'''
        return self.q1.empty()
