def safe_print_division(a, b):
  result= a/b
  while True:
    try:
      safe_print_division(a, b)
      break
    except ZeroDivisionError as result:
    
      print("{:d} / {:d} = {}".format(a, b, None))
      
      break
    
    finally:
      print("{:d} / {:d} = {}".format(a, b, result))
      break
      