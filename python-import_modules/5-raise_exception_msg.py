def raise_exception_msg(message=""):
  
  try:
    message="c is fun"
    raise_exception_msg(message)
  except NameError as err:
    print(err)
  

print(raise_exception_msg("orp"))