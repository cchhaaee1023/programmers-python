def solution(numbers):
    answer = 0

    dict = {}
    for i in numbers:       # 딕셔너리에 등록
        if i not in dict:
            dict[i] = 1
    
    for i in range(10):
        if i not in list(dict.keys()):
            answer += i
            
    return answer