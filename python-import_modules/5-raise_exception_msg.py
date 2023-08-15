def raise_exception_msg(message=""):
     
  try:
    
    message="Python is cool"
    raise NameError(message)
  except NameError as err:
    print(err)
  try:
    
    message=""
    raise NameError(message)
  except NameError as err:
    print(err)
  try:
    
    message="C is fun"
    raise NameError(message)
  except NameError as err:
    print(err)  
  

