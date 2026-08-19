def solution(people, limit):
    count = 0
    weight = 0
    
    people.sort(reverse=True)
    lenp = len(people) - 1
    i = 0
    
    while i < lenp: 
        if people[i] + people[lenp] > limit:
            count += 1
            i += 1
        elif people[i] + people[lenp] <= limit:
            count += 1
            lenp -= 1
            i += 1
        if i == lenp:
            count += 1
            
    return count
        