#!/usr/bin/python3
#encryptdecrypt.py

#Takes the input_text and encrypts it, returning the result
def encryptText(input_text,key):
	input_text=input_text.upper()
	result = ""
	for letter in input_text:
		ascii_value=ord(letter)
		if (ord("A") > ascii_value) or (ascii_value > ord("Z")):
			result+=letter
		else:
			key_val = ascii_value+key
			if not((ord("A")) < key_val < ord("Z")):
				key_val=ord("A")+(key_val-ord("A"))%(ord("Z")-ord("A")+1)
			result+=str(chr(key_val))
	return result
def main():
	print ("Please enter text to scramble:")
	#Get user input
	try:
		user_input = input()
		scrambled_result = encryptText(user_input,10)
		print ("Result: " + scrambled_result)
		print ("To un-scramble, press enter again")
		input()
		unscrambled_result = encryptText(scrambled_result,-10)
		print ("Result: " + unscrambled_result)
	except UnicodeDecodeError:
		print ("Sorry, Only ASCII Characters are supported")

if __name__=="__main__":
	main()

