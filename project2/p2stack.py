"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date: 11/01/2021
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0, size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        return self.numElems == len(self.stack)  # Compare the number of elements in the stack with the stack size.

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        return self.numElems == 0  # Compare the number of elements in the stack with 0.

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        size = len(self.stack)
        backup = self.stack  # Copy the original stack to backup.
        self.stack = [None for x in range(0, 2 * size)]  # Double the size of the stack and fill it with None values.
        self.stack[0:size] = backup  # Give the copy back to the first half of the stack.
        return

    """
    push function to push a value onto the stack.
    Note: val is the value to be pushed onto the top of the stack.
    """
    def push(self, val):
        if self.isFull():
            self.resize()  # Resize the stack if it is full.
        self.top = self.top + 1  # Move the top one index forwards to the position to save the value.
        self.stack[self.top] = val  # Save the value at index top.
        self.numElems = self.numElems + 1  # Increase the number of elements in the stack by one.
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ans = self.stack[self.top]  # Copy the top value to be returned.
        self.stack[self.top] = None  # Remove the top value from the stack.
        self.top = self.top - 1  # Move the top one index backwards.
        self.numElems = self.numElems - 1  # Decrease the number of elements in the stack by one.
        return ans  # Return the top value.
