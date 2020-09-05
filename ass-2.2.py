starting_range= int(input("ENTER THE STARTING RANGE: "))  
last_range = int(input("ENTER THE LAST RANGE: ")) 
print(range(starting_range,last_range)) 
  
for number in range(starting_range,last_range + 1):  
   if number > 1:  
       for i in range(2,number):  
           if (number % i) == 0:  
               break  
       else:  
           print(number)  