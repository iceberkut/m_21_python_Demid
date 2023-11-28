def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
        # sequence = sequence + [next_element] - создается копия sequence, а append меняет текущее состояние
