def is_prime(number):
    # Ensuring that the number is greater than 1
    if number <= 1:
        return False
    
    # Checking for factors from 2 up to the number itself (excluding the number)
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True