def raise_exception_msg(message=""):
    
    try:
      raise_exception_msg("c is fun")
      
    except  NameError as ne:
      print(ne)
      
print(raise_exception_msg("c is fun"))