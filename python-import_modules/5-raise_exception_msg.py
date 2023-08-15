def raise_exception_msg(message=""):
  
  try: 
    raise_exception_msg(message)
    raise NameError(message)
  except NameError as err:
    print(err)
  

