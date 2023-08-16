
def safe_print_division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Division by zero not allowed.")
        
        result = int(a) / int(b)
       
    except ZeroDivisionError:
        result = None
      
    finally:
        print("Inside result: {}".format(result))
      
    return result
safe_print_division(10,2)