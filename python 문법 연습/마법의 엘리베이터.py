def solution(storey):
    answer = 0

    while storey > 0:
        num = storey % 10
        storey = storey // 10
        if num > 5:
            answer += 10 - num
            storey += 1
        elif num == 5:
            if storey % 10 > 4:
                answer += 10 - num
                storey += 1
            else:
                answer += num
        else:
            answer += num

    return answer


print(solution(97))
