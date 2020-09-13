def isPrime(num):
    for i in range(2,num):
        if (num%i)==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(1,2500))
print ('Prime numbers between 1-2500:', list(fltrObj))