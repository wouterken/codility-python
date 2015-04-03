# Author: Wouter Coppieters
def solution(X, A):
    # write your code in Python 2.6
    frog, leaves = 0, [False] * (X)
    for minute, leaf in enumerate(A):
        if leaf <= X:
            leaves[leaf - 1] = True
        while leaves[frog]:
            frog += 1
            if frog == X: return minute
    return -1


#print solution(5, [1, 3, 9, 4, 2, 3, 5, 4])