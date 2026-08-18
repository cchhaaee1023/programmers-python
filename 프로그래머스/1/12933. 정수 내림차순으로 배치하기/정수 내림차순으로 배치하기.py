def solution(n):
    
    
    ml = sorted(str(n), reverse=True)
    print(ml)
    j = "".join(ml)

    return int(j)