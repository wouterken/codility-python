# Author: Wouter Coppieters
def solution(A):
    from collections import defaultdict
    from Queue import Queue
    nodes = defaultdict(dict)
    left = None
    first = None
    for right in A:
        if left != None:
            nodes[left][right] = nodes[right]
            nodes[right][left] = nodes[left]
        else:
            first = right
        left = right
    if left == first:
        return 1
    stack = Queue()
    stack.put((nodes[first], 1))
    while stack.qsize():
        evaluate, depth = stack.get()
        if 'visited' in evaluate:
            continue
        for index, item in evaluate.items():
            if index == left:
                return depth + 1
            stack.put((item, depth + 1))
        evaluate['visited'] = True
    return 1


