def solution(s):
    c = 0
    count_zero = 0
    
    while s != '1':
        count_zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        c += 1
    
    return [c, count_zero]