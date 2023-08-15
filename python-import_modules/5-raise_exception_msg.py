def raise_exception_msg(message=""):
  
  try: 
    message="c is fun"
    raise NameError(message)
  except NameError as err:
    print(err)
  

