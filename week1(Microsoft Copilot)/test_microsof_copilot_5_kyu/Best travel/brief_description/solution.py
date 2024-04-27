import itertools

def choose_best_sum(t, k, ls):
    # Generate all combinations of k towns
    possible_trips = list(itertools.combinations(ls, k))
    
    # Initialize the best sum to be a negative number
    best_sum = -1
    
    # Iterate over all possible trips
    for trip in possible_trips:
        # Calculate the sum of distances for the current trip
        trip_sum = sum(trip)
        
        # If the sum of distances is less than or equal to t and greater than the current best sum
        if trip_sum <= t and trip_sum > best_sum:
            # Update the best sum
            best_sum = trip_sum
    
    # If no trip was found, return None
    if best_sum == -1:
        return None
    
    # Return the best sum of distances
    return best_sum