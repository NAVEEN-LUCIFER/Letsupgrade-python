print(" ENTER THE LIST")
test_list = input() 
sub_list = [1,1,5] 

print ("Original list : " + str(test_list)) 
print ("Original sub list : " + str(sub_list)) 
 
flag = 0
if((set(sub_list) & set(test_list))== set(sub_list)): 
	flag = 1
	
if (flag) : 
	print ("Yes, IT'S A MATCH")
else : 
	print ("No, IT'S GONE ") 
