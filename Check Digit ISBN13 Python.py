#check digit validation ISBN13

numbers = []
string = input("Enter a complete ISBN code (13 digits, including the check digit: \n")
length = len(string)
#this code is used to create a list of integer numbers without the check digit (assumed that the check digit is in position 13 --> position 12 in Python)
for i in range(0,length-1):
  numbers.append(int(string[i]))

#this is used to print numbers of the list
# for num in numbers:
# 	print(num)

#this code is for count the numbers in odd positions and in even positions of the list
even = 0
odd = 0
for i in range(len(numbers)):
	if i%2==1:
		even = even + numbers[i]
	else:
		odd = odd + numbers[i]

even = even*3
total = odd + even
remainder = total % 10
if remainder == 0:
	check_digit = 0
else:
	check_digit = 10 - remainder

print("The check digit for the ISBN code is",check_digit)
