# Author: Wouter Coppieters
def solution(K, T):
	answer, end_points, visited = [], [], [0] * len(T)
	Tree = [{} for i in range(len(T))]

	for index, value in enumerate(T): Tree[index][value], Tree[value][index] = True, True

	root 	   = {'index':K, 'next':None, 'skip':False, 'neighbors':0}
	children   = Tree[root['index']].keys()
	stack 	   = [{'index':child, 'next':root, 'skip':False, 'neighbors':0} for child in children] + [None] * len(T)
	visited[K] = True
	for child in children:
		visited[child] = True

	stack_index, stack_end = 0, len(children)

	while(stack_index < stack_end):
		node, stack_index = stack[stack_index], stack_index + 1

		for child in filter(lambda child: (not visited[child]) and child != node['index'], Tree[node['index']].keys()):
			visited[child], node['neighbors'] = True, node['neighbors'] + 1
			stack[stack_end], stack_end = {'index':child, 'next':node, 'skip':False, 'neighbors':0}, stack_end + 1

		end_points.append(node) if not node['neighbors'] else None

	next_round = sorted(end_points, key=lambda s: -s['index'])

	while len(end_points):
		next_round, end_points = [], next_round
		for point in end_points:
			if point['index'] == K: continue
			elif point['next'] == None or point['next']['index'] == K or (point['next'] and point['next']['neighbors'] > 1):
				answer.append(point['index'])
				if point['next']: point['next']['neighbors'] -= 1
			elif point['index'] != K:
				point['next'] = point['next']['next']
				next_round.append(point)

	return list(reversed(answer + [K]))

print solution(16, [10, 8, 3, 12, 6, 9, 10, 11, 4, 1, 16, 6, 9, 14, 10, 1, 16])
