def raise_exception_msg(message=""):
  
  try: 
    message=""
    raise NameError(message)
  except NameError as err:
    print(err)
  

