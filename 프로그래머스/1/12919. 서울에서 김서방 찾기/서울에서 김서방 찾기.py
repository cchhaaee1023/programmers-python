def solution(seoul):
    answer = ''
    for i, name in enumerate(seoul):
        if name == 'Kim':
            answer = str(i)

    return "김서방은 " + answer + "에 있다"