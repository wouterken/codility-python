# Author: Wouter Coppieters
def solution(A):
    total, length, left_index = A[0], 1, 0
    min_average, min_index = float('inf'), float('inf')

    for index, (left, right) in enumerate(zip(A[:-1],A[1:])):
        total, length = total + right, length + 1
        average = total / float(length)
        if (left + right)/ 2.0 <= average:
            total, length = (left + right), 2
            average = total / float(length)
            left_index = index

        if average < min_average:
            min_average, min_index = average, left_index
    return min_index


print solution([10, 10, -1, 2, 4, -1, 2, -1]) #5