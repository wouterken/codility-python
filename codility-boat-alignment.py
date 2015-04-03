# Author: Wouter Coppieters
def solution(R, X, M):
    top, solution, space_available = None, 0, 0
    if len(R) * (2*X) > M: return -1

    for boat_position in R:
        boat, move_right = boat_position, 0

        if not top:
          index = max(boat, X)
          top = {'left':index - X, 'right': index + X, 'previous':top, 'max':0, 'min':boat - index}
          space_available = index - X
          solution = abs(boat - index)
          continue

        boat = max(X, min(M - X, boat))
        overlap = (top['right']) - (boat - X)
        midpoint = ceil(overlap/2.0)

        if overlap > 0:
          space_right = M - (boat+X)
          move_right = space_right if space_right < midpoint else midpoint
          space_right -= move_right
          overlap -= move_right
          boat += move_right

          while overlap and	space_available:
            gap = top['left'] - (top['previous']['right'] if top['previous'] else 0)
            diff = ceil((top['max'] + overlap + move_right) / 2)
            adjust_right = min(space_right, diff - move_right) if space_right and diff - move_right > 0 else 0
            boat += adjust_right
            move_right += adjust_right
            space_right -= adjust_right
            move_left = min(gap, overlap) - adjust_right
            overlap -= adjust_right + move_left
            space_available -= move_left
            top['max'] += move_left
            top['right'] -= move_left
            top['left'] -= move_left

            if move_left == gap and top['previous']:
              top, rightboats = top['previous'], top
              top['right'],top['max'] = rightboats['right'], max(top['max'], rightboats['max'])

          boat += overlap

        if not (boat - X) - top['right']:
          top['right'], top['min'] = boat + X, max(top['min'], boat - boat_position)
        else:
          top, space_available = {'left':boat - X, 'right': boat + X, 'previous':top, 'max':0, 'min':0}, space_available + (boat - X) - top['right']

        solution = max(solution, max(top['max'], abs(top['min'])))

    return int(solution)
