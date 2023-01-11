def solution(t, p):
  answer = 0
  start = 0
  end = len(p)

  while (end <= len(t)):
    if (int(t[start:end]) <= int(p)):
      answer += 1
    start += 1
    end += 1
  
  return answer

print(solution("50022083987", '7'))