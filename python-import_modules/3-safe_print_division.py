
def safe_print_division(a, b):
 
    try:
        result = int(a) /int(b)
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        
        
   
    else:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        
    finally:
          
      pass

