# Author: Wouter Coppieters
def solution(N, A, B, C):
  tokens = [[[0,-float('inf')]] for n in xrange(N)]
  C = sorted([(item, index) for index, item in enumerate(C)])

  maxlength = 0
  to_remove = []
  for attractiveness, index in C:
    frm, to = A[index], B[index]
    left_token, right_token = None, None

    if frm == to:
      best_token = None

      to_remove = []
      for token in tokens[frm]:
        if token[1] < attractiveness:
          if best_token:
            if best_token[0] < token[0]:
              best_token = token
          else:
            best_token = token

      if best_token:
        left_token = best_token
        maxlength = max(maxlength, best_token[0] + 1)

    else:
      to_remove = []
      best_token = None
      for token in tokens[frm]:
        if token[1] < attractiveness:
          if best_token:
            if best_token[0] < token[0]:
              best_token = token
          else:
            best_token = token

      if best_token:
        left_token = best_token
        maxlength = max(maxlength, best_token[0] + 1)

      best_token = None
      for token in tokens[to]:
        if token[1] < attractiveness:
          if best_token:
            if best_token[0] < token[0]:
              best_token = token
          else:
            best_token = token

      if best_token:
        right_token = best_token
        maxlength = max(maxlength, best_token[0] + 1)

    if left_token:
      tokens[to].append([left_token[0] + 1, attractiveness])
      tokens[frm] = filter(lambda x: x[1] >= attractiveness or x == left_token, tokens[frm])
    if right_token:
      tokens[to] = filter(lambda x: x[1] >= attractiveness or x == right_token, tokens[to])
      tokens[frm].append([right_token[0] + 1, attractiveness])

  return maxlength
