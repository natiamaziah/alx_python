def safe_print_division(a, b):
  result= a/b
  try:
    return result
  except:
   
    print("{:d} / {:d} = {}".format(a, b, result))
    return None
  finally:
    print("{:d} / {:d} = {}".format(a, b, result))
    