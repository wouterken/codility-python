# Author: Wouter Coppieters
def solution(S, P, Q):
    table, charmap = {1:[0], 2:[0], 3:[0], 4:[0]}, {'A':1, 'C':2, 'G':3, 'T':4}
    for char in S:
        for charvalue, prefixsums in table.items():
            prefixsums.append( prefixsums[-1] + charvalue if charvalue == charmap[char] else prefixsums[-1])
    results = []
    for left, right in zip(P, Q):
        for i in range(4):
            if(table[i + 1][left] - table[i + 1][right + 1]):
                results.append(i + 1)
                break

    return results


print solution('GACACCATA', [0, 0, 4, 7], [8, 2, 5, 7])