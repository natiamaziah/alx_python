def no_c(my_string):
  del_c="c","C"
  str2=""
  for char  in my_string:
    if char not in del_c:
      str2=str2+char
  
  return my_string
  
         
         

