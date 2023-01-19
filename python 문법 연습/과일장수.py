def solution(k, m, score):
  answer = 0

  score.sort()

  for i in range(0, int(len(score)/m)):
    for j in range(0, m):
      if j == m - 1:
        answer += score.pop() * m
      else:
        score.pop()

  return answer

print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))