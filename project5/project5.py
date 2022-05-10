"""
Math 560
Project 5
Fall 2021

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date: 12/01/2021
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm: the prim function that assign the proper vertex.prev values to every vertex.

INPUTS
adjList: the adjacency list for the map (a list of Vertex objects).
adjMat: the adjacency matrix for the map.
"""
def prim(adjList, adjMat):
    # Initialize all visited to false, costs to math.inf and prev to null.
    for vertex in adjList:
        vertex.visited = False
        vertex.cost = math.inf
        vertex.prev = None
    # Pick the first vertex in adjList as the start vertex and set cost to 0.
    start = adjList[0]
    start.cost = 0
    # Make the priority queue using cost for sorting.
    Q = PriorityQueue(adjList)
    while not Q.isEmpty():
        # Get the next unvisited vertex and visit it.
        v = Q.deleteMin()
        v.visited = True
        # For each edge out of v.
        for neighbour in v.neigh:
            # If the edge leads out, update.
            if not neighbour.visited:
                # Get the edge between two vertices from adjMat
                if neighbour.cost > adjMat[v.rank][neighbour.rank]:
                    neighbour.cost = adjMat[v.rank][neighbour.rank]
                    neighbour.prev = v
    return

################################################################################

"""
Kruskal's Algorithm: the kruskal function that return a list of edges that are in the MST.

INPUTS
adjList: the adjacency list for the map (a list of Vertex objects).
edgeList: the list of Edge objects for the map.

OUTPUTS
X: the  list of edges that are in the MST.

Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    # Initialize all singleton sets for each vertex.
    for vertex in adjList:
        makeset(vertex)
    # Initialize the empty MST.
    X = []
    # Sort the edges by weight.
    edgeList.sort()
    # Loop through the edges in increasing order.
    for e in edgeList:
        # If the min edge crosses a cut, add it to our MST.
        u, v = e.vertices
        if find(u) != find(v):
            X.append(e)
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    # If we are not at the root.
    if v != v.pi:
        # Set our parent to be the root,
        # which is also the root of our parent!
        v.pi = find(v.pi)
    # Return the root, which is now our parent!
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    # Find the root of the tree for u.
    ru = find(u)
    # Find the root of the tree for u.
    rv = find(v)
    # If the sets are already the same, return.
    if ru == rv:
        return
    # Make shorter set point to taller set.
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # Same height, break tie.
        ru.pi = rv
        # Tree got taller, increment rv.height.
        rv.height += 1
    return

################################################################################

"""
TSP: the tsp function that trace the TSP tour using depth first search on the MST.

INPUTS
adjList: the adjacency list for the map (a list of Vertex objects).
start: the start point of the TSP tour.

OUTPUTS
tour: the tour array of vertex ranks.
"""
def tsp(adjList, start):
    # Iterate through the list of vertices and mark them all as unvisited.
    for vertex in adjList:
        vertex.visited = False
    tour = []
    # Use a stack to track the next unvisited vertex for DFS.
    vertexStack = []
    # Push the start vertex into the top of the stack.
    vertexStack.append(start.rank)
    while len(vertexStack) != 0:
        # Get the vertex at the top of the stack and mark it as visited.
        cur = vertexStack.pop()
        adjList[cur].visited = True
        # Add the vertex into our tour array.
        tour.append(cur)
        # The list of neighbors in the MST.
        for neighbour in adjList[cur].mstN:
            # Push neighbours into the top of the stack if unvisited.
            if not neighbour.visited:
                vertexStack.append(neighbour.rank)
    # The tour must end at the start vertex to complete the cycle.
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False  # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
