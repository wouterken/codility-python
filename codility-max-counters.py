# Author: Wouter Coppieters
def solution(N, A):
    counters = [0] * N
    max_value, threshold = 0, 0
    for a in A:
        index = a - 1
        if index == N:
            threshold = max_value
        else:
            counters[index] = max(threshold + 1, counters[index] + 1)
            max_value = max(max_value, counters[index])
    for index, counter in enumerate(counters):
        counters[index] = max(threshold, counter)
    return counters


print solution(5, [3, 4, 4, 6, 1, 4, 4])