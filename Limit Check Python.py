#limit check implemented in Python

#limit check applied at a lower bound

lower = int(input("Enter the lower bound: "))
flag = True
while flag == True:
	number = float(input("Enter a number: "))
	if number >= lower:
		print("The number is accepted")
		flag = False
	else:
		print("The number is not accepted. Try again")
	
#limit check applied to an upper bound

upper = int(input("Enter the lower bound: "))
flag = True
while flag == True:
	number = float(input("Enter a number: "))
	if number <= upper:
		print("The number is accepted")
		flag = False
	else:
		print("The number is not accepted. Try again")
