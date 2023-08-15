def raise_exception_msg(message=""):
  
  try:
    raise NameError("c is fun")
  except NameError as err:
   return err
  

