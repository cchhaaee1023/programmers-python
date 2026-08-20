def solution(a, b, c, d):
    dice = sorted([a,b,c,d])
    count_same = 0

    uniq = list(set(dice))
    
    
    match len(uniq):
        case 1:
            count_same = 4
        case 2:
            count_same = 2
        case 3:
            count_same = 1
        case 4:
            count_same = 0
            

    if count_same == 4:
        return 1111*a
    
    elif count_same == 2:
        if dice.count(dice[0]) == 3:
            p = dice[0]
            q = dice[3]
        elif dice.count(dice[3]) == 3:
            p = dice[3]
            q = dice[0]
        else:
            return (uniq[0] + uniq[1]) * abs(uniq[0] - uniq[1])
        
        return (10 * p + q)**2
    
    elif count_same == 1:
        for u in uniq:
            if dice.count(u) == 2:
                uniq.remove(u)
                # uniq.remove(u)
        return uniq[0] * uniq[1]
    
    else:
        return min(dice)
        
        