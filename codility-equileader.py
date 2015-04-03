# Author: Wouter Coppieters
def solution(A):
    def get_leader(A):
        from collections import defaultdict
        stack, leaders = [], []
        counts = defaultdict(int)
        for index, a in enumerate(A):
            counts[a] += 1
            stack.append(a)
            while len(stack) > 1 and stack[-1] != stack[-2]:
                stack.pop(),stack.pop()
            leaders.append(stack[-1] if( stack and counts[stack[-1]] > (index + 1)/2.) else -1)
        return leaders
    return len(filter(lambda x: x[0] == x[1] and x[0] != -1, zip(get_leader(A), list(reversed(get_leader(reversed(A))))[1:])))

print solution([1, 2, 3, 4, 5])