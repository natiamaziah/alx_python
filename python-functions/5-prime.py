def is_prime(number):
   while (number/number==1) and (number/1==number):
     if number==3 or number==2:
       return True
     if number%2==0:
       return False
     else:
       return True
  
