"""
Math 560
Project 4
Fall 2021

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date: 11/16/2021

"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function that determine the number of edits required to convert one string into the other.

INPUTS
src: the original string.
dest: the destination string.
prob: specify it is an 'ED' problem or an 'ASM' problem.

OUTPUTS
dist: the number of edits required to convert src into dest, where edits can be insertions, deletions, or substitutions.
edits: the 3-tuple list of specific edits to perform, with components:
        0. One of the following strings: `insert', `delete', `sub', `match'.
        1. The char to be inserted, deleted, substituted, or matched (for substitution, note
        that the letter should be the new letter that replaces the old one).
        2. The index of this edit/match in the original string.
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    else:
        l1 = len(src)
        l2 = len(dest)
        # Construct the DP table, which has l1 rows and l2 columns.
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        # Fill the first column of the table with i in ascending order.
        for i in range(l1 + 1):
            dp[i][0] = i
        # Fill the first row of the table.
        for j in range(l2 + 1):
            # If it is an 'ED' problem, fill with j in ascending order.
            if prob == 'ED':
                dp[0][j] = j
            # If it is an 'ASM' problem, fill with 0s.
            else:
                dp[0][j] = 0
        # Fill the DP table from dp[0][0] to dp[l1][l2].
        for i in range(l1):
            for j in range(l2):
                # Match: go diagonal to lower right.
                if src[i] == dest[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                # Find the choice with the shortest distance among insertion, deletion, and substitution:
                # Insertion: go right, distance + 1.
                # Deletion: go down, distance + 1.
                # Substitution: go diagonal to lower right, distance + 1.
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], min(dp[i + 1][j], dp[i][j]))
        # Get the distance from [0][0] to [l1][l2], which represents the minimum set of edits.
        dist = dp[l1][l2]

        # Go backwards from dp[l1][l2] to dp[0][0] to get the optimal set of edits, starting from the end of the string.
        edits = []
        index1 = l1 - 1
        index2 = l2 - 1

        while index1 != -1 or index2 != -1:
            # Arrive at the start of src, then all the remaining edits would be insertions.
            if index1 == -1:
                while index2 != -1:
                    edits.append(('insert', dest[index2], 0))
                    index2 -= 1
            # Arrive at the start of dest, then all the remaining edits would be deletions.
            elif index2 == -1:
                while index1 != -1:
                    edits.append(('delete', src[index1], index1))
                    index1 -= 1
            # Match: go diagonal to upper left.
            elif src[index1] == dest[index2]:
                edits.append(('match', src[index1], index1))
                index1 -= 1
                index2 -= 1
            else:
                # Find the choice with the shortest distance among insertion, deletion, and substitution.
                temp = min(dp[index1][index2 + 1], min(dp[index1 + 1][index2], dp[index1][index2]))
                # Deletion: go up.
                if temp == dp[index1][index2 + 1]:
                    edits.append(('delete', src[index1], index1))
                    index1 -= 1
                # Insertion: go left.
                elif temp == dp[index1 + 1][index2]:
                    edits.append(('insert', dest[index2], index1 + 1))
                    index2 -= 1
                # Substitution: go diagonal to upper left.
                else:
                    edits.append(('sub', dest[index2], index1))
                    index1 -= 1
                    index2 -= 1
    return dist, edits


################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(True)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
