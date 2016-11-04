
# Finding all prime numbers between 0 to a given number

input = int(raw_input("Enter a non-zero range :> "))
prime = []

def print_prime(var):	
	i = 1 
	while i <= var :
		if (var % i)== 0:
			prime.append(i)
		i+=1		
	
	if len(prime) == 2 or len(prime) == 1 :		
		print var		
	
	del prime [:]
			

for j in xrange(1,input+1):	
 	print_prime(j)
 	


