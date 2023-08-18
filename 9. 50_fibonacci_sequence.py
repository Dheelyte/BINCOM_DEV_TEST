def fibonacci_sum(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    
    return sum(fib_sequence)

num_terms = 50
fibonacci_sum_50 = fibonacci_sum(num_terms)
print("Sum of the first", num_terms, "Fibonacci terms:", fibonacci_sum_50)