
def safe_print_division(a, b):
    


    result=safe_print_division(a,b)

    try:
            safe_print_division(a,b)
    except:
          print("Inside result: None")
          
    finally:
              print("Inside result: {:f}".format(result))
              print("{:d} / {:d} = {:f}".format(a, b, result))
    return a/b
          