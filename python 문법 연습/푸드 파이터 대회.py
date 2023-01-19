def solution(food):
  left = ''
  right = ''

  for i in range(1, len(food)):
    if food[i] % 2 == 1:
      food[i] -= 1
    left += str(i) * int(food[i] / 2)
    right = str(i) * int(food[i] / 2) + right
  
  return left + '0' + right

print(solution([1,7,1,2]))
