def safe_print_division(a, b):
  result= a/b
  try:
    safe_print_division(a, b)
  except ZeroDivisionError:
   
    print("{:d} / {:d} = {}".format(a, b, result))
    
  finally:
    print("{:d} / {:d} = {}".format(a, b, result))
    