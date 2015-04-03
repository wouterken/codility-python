# Author: Wouter Coppieters
def solution(A):
    right,total = 0,0
    for left in A:
        right, total = (right + 1, total) if not left else (right, total + right)
    return total if total < 1000000000 else -1

