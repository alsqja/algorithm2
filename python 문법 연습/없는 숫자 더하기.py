def solution(numbers: list):
    return sum(numbers.count(el) == 0 and el for el in range(10))


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
