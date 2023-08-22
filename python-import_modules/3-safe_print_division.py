
def safe_print_division(a, b):
    try:
       
        if b == 0:
            raise ZeroDivisionError("Division by zero not allowed.")
        result = int(a) / int(b)
        
    except ZeroDivisionError as e:
        result = None
       
    '''finally:
        
     
      print("Inside result: {}".format(result))
      
      
    return result'''


   