# Author: Wouter Coppieters
def solution(A, B):
    heighest = 0
    heights = []
    for height in A:
        heighest, old = max(height, heighest), heighest
        heights.append(heighest)

    current = 0
    points = [0] * (max(heights) + 1)
    for index, height in enumerate(heights):
        if current != height:
            for i in xrange(current + 1, height + 1 , 1):
                points[i] = index
            current = height

    for ball in B:
        index = (points[ball] if len(points) > ball else 0) - 1
        if index == -1:
            continue
        A[index] += 1
        dropped_height = A[index]

        if points[dropped_height] > index:
            points[dropped_height] = index
    return A

