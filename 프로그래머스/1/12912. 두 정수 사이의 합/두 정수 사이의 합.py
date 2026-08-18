def solution(a, b):
    answer = 0
    if a > b:   # 무조건 b가 큰 값이 되도록 바꿈
        a, b = b, a
    
    for i in range(b - a + 1):
        answer += i + a
    return answer