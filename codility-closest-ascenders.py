# Author: Wouter Coppieters
def solution(A):
    ret = []
    for left,right in zip(get_closest_ascenders(A) ,list(reversed(get_closest_ascenders(list(reversed(A)))))):
        value = min(left, right)
        ret.append(0 if value == float('inf') else value)
    return ret

def get_closest_ascenders(A):
    stack = [0] * len(A)
    ascenders = [0] * len(A)
    stack_index = -1
    for index, a in enumerate(A):
        while stack_index > -1 and A[stack[stack_index]] <= a:
            stack_index -= 1
        if stack_index == -1:
            ascenders[index] = float('inf')
        else:
            ascenders[index] = index - stack[stack_index]
        stack_index += 1
        stack[stack_index] = index
    return ascenders


print solution([4, 3, 1, 4, -1, 2, 1, 5, 7])