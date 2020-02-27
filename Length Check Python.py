#length check validation using Python

min_characters = int(input("Introduce the minimum characters allowed: "))
max_characters = int(input("Introduce the maximum characters allowed: "))
flag = True
while flag == True:
	string = input("Enter a word or sentence: ")
	length = len(string)
	if length >= min_characters and length <= max_characters:
		print("The length of the string is allowed. ")
		flag = False
	else:
		print("The length of the string is not allowed. Try again.")
