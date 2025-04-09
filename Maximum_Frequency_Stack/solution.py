'''Solution for Maximum Frequency Stack problem on LeetCode
https://leetcode.com/problems/maximum-frequency-stack/submissions/1602048861/
'''
from collections import deque, defaultdict

class FreqStack:
    '''Class to implement a stack that supports push, pop, 
    and retrieving the most frequent element.'''

    def __init__(self):
        self.stacks = defaultdict(deque)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''Pushes an integer onto the stack.'''
        self.freq[val] += 1

        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]

        self.stacks[self.freq[val]].append(val)

    def pop(self) -> int:
        '''Pops and returns the most frequent element.'''
        val = self.stacks[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return val
