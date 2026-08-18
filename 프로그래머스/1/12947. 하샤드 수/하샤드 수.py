def solution(x):
    s = sum(map(int, str(x)))
    if x % s == 0:
        return True
    else:
        return False