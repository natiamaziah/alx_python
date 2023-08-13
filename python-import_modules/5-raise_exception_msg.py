def raise_exception_msg(message=""):
    try:
      ans=raise_exception_msg("C is fun")
      print(ans)
    except NameError as e:
      print(e)
      
