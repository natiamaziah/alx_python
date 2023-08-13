def safe_print_division(a, b):
      result=safe_print_division
      try:
            result=a/b
      except:
             print("Inside result: None")
             print("{:d} / {:d} = {}".format(a, b, None))
      finally:
            print("Inside result: {:f}".format(result))
            print("{:d} / {:d} = {:f}".format(a, b, result))

print(safe_print_division(10,0))