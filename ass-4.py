lower = int(input("ENTER THE LOWER RANGE: "))  #inupt values
upper = int(input("ENTER THE UPPER RANGE: "))  
print(range(lower,upper))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:    #while_loop
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:     
       print(num)
       break            #this break statement is used to break the loop. when the first armstrong number is been printed.