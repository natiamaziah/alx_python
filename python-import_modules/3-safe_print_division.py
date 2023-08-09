
def safe_print_division(a, b):
  
  result=safe_print_division(a,b)
  try:
      safe_print_division(a,b)
  except:
      print("{:d} / {:d} = {}".format(a, b,result ))
  finally:
      print("{:d} / {:d} = {}".format(a, b, result))
      return result
      