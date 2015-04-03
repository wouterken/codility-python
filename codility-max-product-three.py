# Author: Wouter Coppieters
def solution(A):
    index_pairs = list(sorted(((a, index) for index,a in enumerate(A))))
    return max(index_pairs[-1][0] * index_pairs[-2][0] * index_pairs[-3][0],index_pairs[-1][0] * index_pairs[0][0] * index_pairs[1][0])
