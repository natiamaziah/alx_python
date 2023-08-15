def raise_exception_msg(message=""):
  
  try: 
    message="python is cool"
    raise NameError(message)
  except NameError as err:
    print(err)
  

