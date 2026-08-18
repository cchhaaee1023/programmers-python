def solution(s):
    count = 0
    li = list(s)
    
    if li[0] != '(':
        return False
    if li[-1] != ')':
        return False
    
    for i in li:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                return False
        
    if count != 0:
        return False
    
    return True