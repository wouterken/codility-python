# Author: Wouter Coppieters
def solution(A):
    minimum, maxprofit = float('inf'), 0
    for value in A:
        minimum = min(value, minimum)
        maxprofit = max(value - minimum, maxprofit)
    return maxprofit

print solution([4,5,6,9,1,10])