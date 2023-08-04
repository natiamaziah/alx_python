def fibonacci_sequence(n):
    result = []
    a,b=0,1
    while len(result) < n:
        result.append(a)
        a,b=b,a+b
    return result

print(fibonacci_sequence(6))


