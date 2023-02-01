def solution(x, y, n):
    answer = 0
    arr = [1, 2, 3]

    def calculator(a, b, n):
        if b == 1:
            return a + n
        elif b == 2:
            return a * 2
        elif b == 3:
            return a * 3

    def dfs(a, num, answer):
        for i in arr:
            cal = calculator(a, i, n)
            if cal > y:
                return 0
            if cal == y:
                if answer > num:
                    answer = num
                return answer
            else:
                num += 1
                print(cal, i, num)
                dfs(cal, num, answer)
        return answer

    answer = dfs(x, 0, answer)

    if answer == 0:
        return -1

    return answer


print(solution(10, 40, 5))


def solution(x, y, n):
    dp = [1000001] * (y + 1)
    dp[x] = 0
    for i in range(x, y + 1):
        if dp[i] == 1000001:
            continue
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == 1000001:
        return -1
    else:
        return dp[y]


from collections import deque


def solution(x, y, n):
    num = 0
    stack = deque([[y, 0]])
    while stack:
        y, num = stack.popleft()
        if y == x:
            return num
        if y < x:
            continue

        if y % 2 == 0:
            stack.append([y / 2, num + 1])
        if y % 3 == 0:
            stack.append([y / 3, num + 1])
        stack.append([y - n, num + 1])

    return -1
