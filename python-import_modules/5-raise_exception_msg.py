def raise_exception_msg(message=""):
     
  try:
    if message=="C is fun":
       raise NameError(message)
    elif message=="":
       raise NameError(message)
    else:
       raise NameError("Python is cool")
  except NameError as err:
    print(err)
  

  

