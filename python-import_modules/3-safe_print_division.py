
def safe_print_division(a, b):
 
    try:
        result = int(a) /int(b)
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        print("{:d} / {:d} = {}".format(a, b,None))
        return None
    except TypeError:
        print("Both inputs must be integers")
        return None
    else:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        return result
    finally:
          
      pass
# Example usage
safe_print_division(10, 2)