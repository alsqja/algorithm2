def solution(k, score):
  answer = []

  best = []

  for i in range(0, len(score)):
    if (len(best) < k) :
      best.sort(reverse = True)
      best.append(score[i])
      best.sort(reverse = True)
      answer.append(best[-1])
    else:
      best.sort(reverse=True)
      if (best[-1] < score[i]):
        best.pop()
        best.append(score[i])
        best.sort(reverse=True)
        answer.append(best[-1])
      else:
        answer.append(best[-1])
  
  return answer

print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))