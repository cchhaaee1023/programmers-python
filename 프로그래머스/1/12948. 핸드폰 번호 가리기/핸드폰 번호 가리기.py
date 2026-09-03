def solution(phone_number):
    answer = ''
    n = len(phone_number)
    
    for i in range(n - 4):
        answer += '*'
    answer += phone_number[n-4:]
    return answer