for i in range(100):
    if i < 10:
        print ("0"),
    print ("{:d}".format(i)),
    if i < 99:
        print (","),