#presence check validation in a string

flag = True
while flag == True:
	string = input("Introduce a word or sentence: ")
	if string != "":
		print("The field has been filled in. ")
		flag = False
	else:
		print("The field is empty. Fill in with some information. ")
