import math

def solution(number, limit, power):
  answer = 0

  def powerMaker(n): 
    result = 0
    for i in range(1, int(math.sqrt(n)) + 1):
      if n % i == 0:
        if (math.sqrt(n) == i):
          result += 1
        else:
          result += 2
        if result > limit:
          return power
    return result
  
  number = list(map(powerMaker, list(range(number + 1))))

  return sum(number)

print(solution(10,3,2))