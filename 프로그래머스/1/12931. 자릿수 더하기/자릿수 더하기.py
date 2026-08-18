def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = n // 10
        # 정수 나누기 안 하면 오류
    
    return answer