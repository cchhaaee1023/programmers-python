def solution(s):
    s = s.lower()
    cp = s.count('p')
    cy = s.count('y')
    
    if cp == cy:
        return True
    else:
        return False