def safe_print_division(a, b):
  result= a/b
  try:
    safe_print_division(a, b)
  except ZeroDivisionError as result:
   
    print("{:d} / {:d} = {}".format(a, b, None))
    return None
  finally:
    print("{:d} / {:d} = {}".format(a, b, result))
    