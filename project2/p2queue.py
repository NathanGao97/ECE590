"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date: 11/01/2021
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        return self.numElems == len(self.queue)  # Compare the number of elements in the queue with the queue size.

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        return self.numElems == 0  # Compare the number of elements in the queue with 0.

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        size = len(self.queue)
        backup = self.queue  # Copy the original queue to backup.
        self.queue = [None for x in range(0, 2 * size)]  # Double the size of the queue and fill it with None values.
        self.queue[0:size] = backup  # Give the copy back to the first half of the queue.
        self.front = 0  # Reset the front to index 0.
        self.rear = size  # Set the rear to index size.
        return

    """
    push function to push a value into the rear of the queue.
    Note: val is the value to be pushed into the rear of the queue.
    """
    def push(self, val):
        if self.isFull():
            self.resize()  # Resize the queue if it is full.
        self.queue[self.rear] = val  # Save the value at index real.
        # Move the rear:
        # one index forwards if it is not at the end of the queue.
        # back to the start of the queue if it is at the end of the queue.
        self.rear = (self.rear + 1) % len(self.queue)
        self.numElems = self.numElems + 1  # Increase the number of elements in the queue by one.
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ans = self.queue[self.front]  # Copy the value from the front to be returned.
        self.queue[self.front] = None  # Remove the value at the front of the queue.
        # Move the front:
        # one index forwards if it is not at the end of the queue.
        # back to the start of the queue if it is at the end of the queue.
        self.front = (self.front + 1) % len(self.queue)
        self.numElems = self.numElems - 1  # Decrease the number of elements in the queue by one.
        return ans  # Return the value from the front.
