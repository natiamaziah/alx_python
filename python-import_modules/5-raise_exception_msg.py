'''def raise_exception_msg(message=""):
    
    try:
      raise_exception_msg("c is fun")
      print("c is fun")
    except  NameError as ne:
      print(ne)
      
print(raise_exception_msg("pyt")) '''


def raise_exception_msg(message=""):
    class NameException(Exception):
        pass
    raise NameException("c is fun")
print(raise_exception_msg("c is fun"))