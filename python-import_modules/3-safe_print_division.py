a=input()
b=input()
def safe_print_division(a, b):
  return a/b
result=safe_print_division(a,b)
try:
    safe_print_division
except:
    print("{:d} / {:d} = {}".format(a, b,result ))
finally:
    print("{:d} / {:d} = {}".format(a, b, result))
    