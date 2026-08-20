def solution(n):
    ml = sorted(str(n), reverse=True)       # list로 저장된다
    j = "".join(ml)

    return int(j)