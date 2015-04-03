# Author: Wouter Coppieters
def solution(H):
    blocks, previous, stack = 0, 0, []
    for current in H:
        if current > previous:
            blocks += 1
        elif current < previous:
            existing = previous
            while len(stack) and stack[-1] >= current:
                existing = stack.pop()
            blocks += 1 if existing != current else 0
        previous = current
        stack.append(previous)
    return blocks





print solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) #7