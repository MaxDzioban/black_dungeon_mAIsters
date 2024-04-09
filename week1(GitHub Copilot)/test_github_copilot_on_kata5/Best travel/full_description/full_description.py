import itertools

def choose_best_sum(t, k, ls):
    max_sum = -1
    for towns in itertools.combinations(ls, k):
        total_distance = sum(towns)
        if total_distance <= t and total_distance > max_sum:
            max_sum = total_distance
    return max_sum if max_sum != -1 else None