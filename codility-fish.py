# Author: Wouter Coppieters
def solution(A, B):
    stack, alive = [], len(A)
    for fish in zip(A, B):
        size, up = fish
        if not up:
            while stack and stack[-1] < size:
                alive -= 1
                stack.pop()
            alive -= 1  if stack else 0
        else:
            stack.append(size)

    return alive



print solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) #2