def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return 5*len(cities)
    
    for i, city in enumerate(cities):
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:   # 캐시에 없음
            if len(cache) == cacheSize:     # 꽉찼을 때
                cache.pop(0) # 가장 오래된 city 삭제
            answer += 5 
            cache.append(city)
    return answer