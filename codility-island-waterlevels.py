# Author: Wouter Coppieters
def solution(A, B):
    water_levels, current_peak, total_peaks = [1] + [0] * max(max(A),max(B)), None, 0

    for previous_water_level, water_level in zip(A[:-1], A[1:]):

        if water_level < previous_water_level:
            current_peak = [water_level, current_peak[1]] if current_peak else [water_level, previous_water_level]

        elif water_level > previous_water_level and current_peak != None:
            water_levels[current_peak[0]] += 1
            water_levels[current_peak[1]] -= 1
            current_peak = None

    water_levels[current_peak[1] if current_peak else water_level] -= 1

    for i, l in enumerate(water_levels): water_levels[i] = total_peaks = total_peaks + l

    return [water_levels[day] for day in B]
