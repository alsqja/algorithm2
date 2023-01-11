def solution(s):
  answer = [-1]

  for i in range(1, len(s)):
    str = s[0: i]
    for j in range(len(str) - 1, -1, -1):
      if (str[j] == s[i]):
        answer.append(i - j)
        break
    if (len(answer) != i + 1):
      answer.append(-1)

  return answer

print(solution('foobar'))