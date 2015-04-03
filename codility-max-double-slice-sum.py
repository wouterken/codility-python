# Author: Wouter Coppieters
def solution(A):
    N, starts, ends = len(A), [0]  * N, [0] * N
    for i in range(1,N-1):
        left, right = i, N-i-1
        starts[left] = max(starts[left - 1] + A[left], 0)
        ends[right] = max(ends[right + 1] + A[right], 0)
    return max((starts[i-1] + ends[i+1] for i in range(1, N-1)))
