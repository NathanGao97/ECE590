"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date: 11/01/2021
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
reset function to reset the maze.

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
maze: A reset maze with vertices initialized as origin. 
"""
def reset(maze):
    for i in range(len(maze.adjList)):
        maze.adjList[i].dist = math.inf  # Reset dist to be infinite.
        maze.adjList[i].visited = False  # No vertex visited.
        maze.adjList[i].prev = None  # No previous node on path yet.
    return


"""
dfsSearch function to find a path in the maze to go from maze.start to maze.exit.

INPUTS
stack: A Stack object which could store vertices in the maze.

OUTPUTS
Attributes of vertices in the maze updated after experiencing a DFS search.
"""
def dfsSearch(stack):
    while not stack.isEmpty():
        cur = stack.pop()  # Remove the value at the top of the stack.
        for i in range(len(cur.neigh)):
            if not cur.neigh[i].visited:
                stack.push(cur.neigh[i])  # Push neighbouring vertices into the top of the stack if not visited.
                cur.neigh[i].visited = True  # The vertex is now visited.
                cur.neigh[i].dist = 1 + cur.dist  # Update its dist.
                cur.neigh[i].prev = cur  # Show its previous node.
        # return dfsSearch(stack)  # Recursive Search until all vertices visited.
    return


"""
bfsSearch function to find a path in the maze to go from maze.start to maze.exit.

INPUTS
queue: A Queue object which could store vertices in the maze.

OUTPUTS
Attributes of vertices in the maze updated after experiencing a BFS search.
"""
def bfsSearch(queue):
    while not queue.isEmpty():
        cur = queue.pop()  # Remove the value at the front of the queue.
        for i in range(len(cur.neigh)):
            if not cur.neigh[i].visited:
                queue.push(cur.neigh[i])  # Push neighbouring vertices into the rear of the queue if not visited.
                cur.neigh[i].visited = True  # The vertex is now visited.
                cur.neigh[i].dist = 1 + cur.dist  # Update its dist.
                cur.neigh[i].prev = cur  # Show its previous node.
        return dfsSearch(queue)  # Recursive Search until all vertices visited.
    return


"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    # If the alg is DFS
    if alg == 'DFS':
        reset(maze)  # Reset the maze.
        dfsStack = Stack()   # Use a stack object to store vertices.
        dfsStack.push(maze.start)  # Push the start vertex into the top of the stack.
        maze.start.visited = True
        maze.start.dist = 0
        dfsSearch(dfsStack)  # Do DFS search to find a path go from maze.start to maze.exit.
        path = []  # Use a python list to store the path from maze.start to maze.exit.
        cur = maze.exit
        while cur.prev is not None:
            path.append(cur.rank)  # Adversely store the path from maze.exit to maze.start.
            cur = cur.prev
        path.append(maze.start.rank)
        path.reverse()  # Reverse the path to go from maze.start to maze.exit.
        return path  # Return the path
    # If the alg is BFS
    else:
        reset(maze)  # Reset the maze
        bfsQueue = Queue()  # Use a queue object to store vertices.
        bfsQueue.push(maze.start)  # Push the start vertex into the rear of the queue.
        maze.start.visited = True
        maze.start.dist = 0
        bfsSearch(bfsQueue)  # Do BFS search to find a path go from maze.start to maze.exit.
        path = []  # Use a python list to store the path from start to exit.
        cur = maze.exit
        while cur.prev is not None:
            path.append(cur.rank)  # Adversely store the path from maze.exit to maze.start.
            cur = cur.prev
        path.append(maze.start.rank)
        path.reverse()  # Reverse the path to go from maze.start to maze.exit.
        return path  # Return the path


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(True)