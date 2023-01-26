def solution(arr1, arr2):

  length1 = len(arr1)
  length2 = len(arr1[0])
  for i in range(0, length1):
    for j in range(0, length2):
      arr1[i][j] += arr2[i][j]

  return arr1

print(solution([[1],[2]], [[3],[4]]))