def solution(absolutes, signs):
    l = list(zip(signs, absolutes))
    answer = 0
    
    for i in l:
        if i[0] == True:
            answer += i[1]
        else:
            answer += i[1]*-1
    
    return answer