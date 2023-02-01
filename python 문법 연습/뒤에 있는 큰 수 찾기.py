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


def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        # 스택에 인덱스가 존재하고, 마지막 인덱스의 숫자가 i번째 숫자보다 작다면
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]  # 스택에서 제외시키고, 해당 인덱스 값을 바꿔주기

        stack.append(i)  # 스택에 인덱스 넣기

    return answer
