
def is_prime(number):
    # Ensuring that the number is greater than 1
    if number <= 1:
        return False
    
    # Checking for factors from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True
  
print(is_prime(3))