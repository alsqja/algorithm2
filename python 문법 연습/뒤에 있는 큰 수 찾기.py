def solution(numbers):
    answer = []
    numberLen = len(numbers)
    maximun = max(numbers)
    for i in range(0, numberLen):
        index = i
        while 1:
            index += 1
            if index == numberLen or numbers[i] == maximun:
                answer.append(-1)
                break
            if numbers[index] > numbers[i]:
                answer.append(numbers[index])
                break

    return answer


print(solution([2, 3, 3, 5]))
