def max_sequence(arr):
    # Initialize max_so_far and max_ending_here
    max_so_far = max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    # Return the maximum sum
    return max_so_far