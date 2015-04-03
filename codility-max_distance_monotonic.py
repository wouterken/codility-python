def solution(A):
	current = None
	left, right = A[0], A[-1]
	ltor, rtol = [(left, 0)],[(right, len(A) - 1)]

	for index in xrange(len(A)):
		rindex = len(A) - index - 1
		if left > A[index]:
			left = A[index]
			ltor.append((left, index))
		if right < A[rindex]:
			right = A[rindex]
			rtol.append((right, rindex))
	
	ltor_index, rng, maxrange = len(ltor) - 1, 0,0

	for rtol_group in rtol:
		right, rindex = rtol_group
		left, lindex = ltor[ltor_index]

		while left <= right:
			if ltor_index == -1: break
			rng = rindex - ltor[ltor_index][1]
			maxrange = max(maxrange, rng)
			ltor_index -= 1
			left, lindex = ltor[ltor_index]
		if ltor_index == -1: break
		while ltor[ltor_index][1] >= rindex:
			ltor_index -= 1
			if ltor_index == -1: break

		

	return maxrange

	
print solution([7, 10, 3, 9, 4, 10, 3, 1])#5
print solution([5, 3, 6, 3, 4, 2])#3
