# Author: Wouter Coppieters
def solution(A):
    stack = []
    for a in A:
        stack.append(a)
        while len(stack) > 1 and stack[-1] != stack[-2]:
            stack.pop(),stack.pop()
    if stack:
        candidate, total = stack[0], 0
        for index, a in enumerate(A):
            total += 1 if  a == candidate else 0
            if total > len(A)/2:
                return index
    return -1
