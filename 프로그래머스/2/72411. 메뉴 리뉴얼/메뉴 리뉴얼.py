from itertools import combinations
def solution(orders, course):
    orders = list(map(lambda x:''.join(sorted(x)), orders))
    result = []
    for cnt in course:
        counter = dict()
        for order in orders:
            tmp = map(lambda x:"".join(x), combinations(order,cnt))
            for t in tmp:
                if t in counter :
                    counter[t] += 1
                else :
                    counter[t] = 1
        if counter:
            maxi = max(counter.values())
            if maxi < 2:
                break
            for c in counter:
                if counter[c] == maxi:
                    result.append(c)
    return sorted(result)
            