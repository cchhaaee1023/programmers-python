def solution(arr, k):
    answer = []
    
    for num in arr:
        if num not in answer and len(answer) < k:
            answer.append(num)
            
    if len(answer) < k :
        for _ in range(k - len(answer)):
            answer.append(-1)
    
    
    return answer