from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    city_arr = []
    for city in cities:
        city_arr.append(city.lower())
    for city in city_arr:
        if cacheSize == 0:
            answer += 5*len(city_arr)
            break
        elif city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(city)
                answer += 5
            else:
                answer += 5
                cache.append(city)
    return answer