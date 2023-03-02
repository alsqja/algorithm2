def solution(cards1: list, cards2: list, goal: list):
    while 1:
        if len(goal) == 0:
            return "Yes"
        str = goal.pop(0)
        if cards1 and cards1[0] == str:
            cards1.pop(0)
        elif cards2 and cards2[0] == str:
            cards2.pop(0)
        else:
            return "No"


print(solution())
