# Author: Wouter Coppieters
def solution(A):
    total, minimum, left = sum(A), float('inf'), 0
    for a in A[:-1]:
        left += a
        minimum = min(abs(total - left - left), minimum)
    return minimum

print solution([3, 1, 2, 4, 3])