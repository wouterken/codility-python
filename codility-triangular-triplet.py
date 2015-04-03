# Author: Wouter Coppieters
def solution(A):
    A = sorted(A)
    for left, mid, right in zip(A[:-2], A[1:-1], A[2:]):
        if left + mid > right and left + right > mid:
            return 1
    return 0

print solution([10, 2, 5, 1, 8, 20])