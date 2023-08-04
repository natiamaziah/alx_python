def fibonacci_sequence(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []* n
    a, b = 0, 1
    while a < n:
        result=result + [a]   # see below
        a, b = b, a+b
    return result
print(fibonacci_sequence(100))