import sys
if __name__=="__main__":
  arg_count=len(sys.argv)-1

  if arg_count==1:
   print("{:d} argument".format(arg_count))
  else:
    print("{:d} arguments:".format(arg_count))
  for index, ele in enumerate(sys.argv[1:],start=1):
      print(f"{index}: {ele}")




   