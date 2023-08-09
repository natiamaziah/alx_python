def raise_exception():
  return
try:
  raise_exception()
except TypeError as te:
  print("Exception has been raised")