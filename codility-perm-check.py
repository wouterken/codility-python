# Author: Wouter Coppieters
def solution(A):
    present = [False] * len(A)
    for a in A:
        if a > len(present):
            return 0
        present[a - 1] = True
    for is_valid in present:
        if not is_valid:
            return 0
    return 1

print solution([4, 1, 3])