def solution(a, b, c, d):
    dice = sorted([a,b,c,d])
    count_same = 0

    uniq = list(set(dice))  

    if len(uniq) == 1:
        return 1111*a
    
    elif len(uniq) == 2:
        if dice.count(dice[0]) == 3:
            p = dice[0]
            q = dice[3]
        elif dice.count(dice[3]) == 3:
            p = dice[3]
            q = dice[0]
        else:
            return (uniq[0] + uniq[1]) * abs(uniq[0] - uniq[1])
        return (10 * p + q)**2
    
    elif len(uniq) == 3:
        for u in uniq:
            if dice.count(u) == 2:
                uniq.remove(u)
        return uniq[0] * uniq[1]
    
    elif len(uniq) == 4:
        return min(dice)
        
        