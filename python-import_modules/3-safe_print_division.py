
def safe_print_division(a, b):
 
    try:
        result = int(a) /int(b)
        if b== 0:
              raise ZeroDivisionError(None)
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        print("{:d} / {:d} = {}".format(a, b, None))
    else:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        
    finally:
          pass