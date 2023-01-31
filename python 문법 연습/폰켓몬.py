def solution(nums):
  s = set()

  for i in nums:
    s.add(i)
  
  if len(s) > len(nums)/2:
    return int(len(nums)/2)
  else:
    return len(s)

print(solution([3,3,3,2,2,2]))