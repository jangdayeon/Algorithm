from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    cities = map(lambda x:x.upper(), cities)
    cache = deque([])
    result = 0
    for city in cities:
        if len(cache) == 0:
            cache.append(city)
            result += 5
            continue
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            result += 5
        else :
            cache.remove(city)
            cache.append(city)
            result += 1
    return result
            