
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
        if b == 0:
            raise ZeroDivisionError("Division by zero not allowed.")
    except ZeroDivisionError as e:
        result = None
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
        print(e)
    else:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
        pass
safe_print_division(10,2)