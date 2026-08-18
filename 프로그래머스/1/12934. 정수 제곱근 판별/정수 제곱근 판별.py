import math
def solution(n):
    answer = 0
    x = math.sqrt(n)
    if x % 1 == 0:
        return (x+1)**2
    else:
        return -1