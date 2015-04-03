# Author: Wouter Coppieters
def solution(S):
    open_brackets, closed_brackets, stack = {'{':1,'[':2,'(':3}, {'}':1,']':2,')':3}, []
    for char in S:
        if char in open_brackets:
            stack.append(open_brackets[char])
        elif not len(stack) or closed_brackets[char] != stack.pop():
                return 0
    return 1 if not len(stack) else 0
