def fibonacci_sequence(n):
    if n <= 0:
        return []

    # Initialize the list with the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence