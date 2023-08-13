def raise_exception_msg(message="c is fun"):
  try:
    raise_exception_msg("C is fun")
  except NameError as ne:
    print(ne)
