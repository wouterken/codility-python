# Author: Wouter Coppieters
def solution(A):
    expected = (len(A)+2) * (len(A) + 1)/2
    for a in A:
        expected -= a
    return expected