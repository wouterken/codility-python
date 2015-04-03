# Author: Wouter Coppieters
def solution(A):
    from collections import defaultdict
    starts, ends, discs, intersects = [0] * len(A), [0] * len(A), 0, 0
    if not len(A):
        return 0
    for index, radius in enumerate(A):
        left, right = index - radius, index + radius
        starts[max(0,left)] += 1
        ends[min(len(A) - 1,right)] += 1

    for i in range(len(A)):
        if starts[i] > 0:
            intersects += discs * starts[i] + (starts[i] * (starts[i] - 1)/2)
            discs += starts[i]
        discs -= ends[i]

    return intersects if intersects <= 10000000 else -1


print solution([1, 5, 8, 7, 8, 4, 8, 5, 0, 5])