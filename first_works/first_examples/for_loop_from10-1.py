def solution(number):
    sum = 0

    for x in range(1, number):
        if x > 0:
            if x % 3 == 0 and x % 5 == 0:
                sum += x
                continue
            elif x % 3 == 0:
                sum += x
            elif x % 5 == 0:
                sum += x
    return sum


print(solution(50))
