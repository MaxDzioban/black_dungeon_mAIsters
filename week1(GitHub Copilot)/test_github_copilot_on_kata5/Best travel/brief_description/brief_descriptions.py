import itertools

def choose_towns(ls, t, num_towns):
    max_distance = 0
    max_combination = None

    # Generate all combinations of towns
    combinations = itertools.combinations(ls, num_towns)

    # Iterate over each combination
    for combination in combinations:
        # Calculate the sum of distances
        distance_sum = sum(combination)

        # Check if the sum is within John's driving limit
        if distance_sum <= t:
            # Update the maximum distance and combination
            if distance_sum > max_distance:
                max_distance = distance_sum
                max_combination = combination

    return max_combination

# Example usage
ls = [50, 55, 57, 58, 60]
t = 174
num_towns = 3

chosen_towns = choose_towns(ls, t, num_towns)
print("Chosen towns:", chosen_towns)