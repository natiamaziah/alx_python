
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
        if b == 0:
            raise ZeroDivisionError("Division by zero not allowed.")
        else:
               print("Inside result: {}".format(result))
               print("{:d} / {:d} = {}".format(a, b, result))
    except ZeroDivisionError as e:
        result = None
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
       
    
       
    finally:
        pass
