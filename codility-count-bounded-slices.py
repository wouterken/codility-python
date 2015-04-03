# Author: Wouter Coppieters
def solution(K, A):
    lindex, left = 0, A[0]
    maxi, mini = -float('inf'), float('inf')
    ranges,maxes,mins,overlaps = [],[],[],[]
    max_index = min_index = 0

    for rindex, right in enumerate(A):

        maxi, mini, prev_max, prev_min = max(maxi, right), min(mini, right), None, None

        while(len(maxes) > max_index and maxes[-1][0] < right): prev_max = maxes.pop()
        while(len(mins) > min_index and mins[-1][0] > right): prev_min = mins.pop()

        maxes.append((right, prev_max[1] if prev_max and prev_max[0] < right else rindex))
        mins.append((right, prev_min[1] if prev_min and prev_min[0] > right else rindex))

        if abs(maxi - mini) > K:

            ranges.append(rindex - lindex)

            if not maxi == right:
                while max_index < len(maxes) and maxes[max_index][0] > mini + K: max_index += 1
                next_point = maxes[max_index]
                maxi, lindex = next_point
            else:
                while min_index < len(mins) and mins[min_index][0] < maxi - K: min_index += 1
                next_point = mins[min_index]
                mini, lindex = next_point

            overlaps.append(rindex - lindex)

    ranges.append(rindex - lindex + 1)

    return min(
                reduce(lambda total, a: total - (a * (a+1))/2, overlaps,
                reduce(lambda total, a: total + (a * (a+1))/2, ranges, 0)),
            1000000000)

#print solution(6, [2, 2, 3, 3, 9, 8, 5, 1, 7, 4, 6, 10]) #40
#print solution(4, [1, 3, -3, -2, -1, 2, 3, 1, 4]) #23
#print solution(2, [3, 5, 7, 6, 3]) #9
#print solution(5, [2, 3, 2, 9, 8, 3, 10, 6, 7, 1, 10, 9]) #21
#print solution(3, [10, 1, 7, 2, 2, 9, 3, 6, 2, 7, 3, 3]) # 15
#print solution(5, [10, 7, 10, 4, 9, 3, 5, 8, 2, 7, 7, 3]) #25
#print solution(6, [4, 5, 8, 5, 1, 4, 6, 8, 7, 2, 2, 5]) # 44