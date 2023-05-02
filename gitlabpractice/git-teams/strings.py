
#Write a function that receives one string as a parameter, return a new
#string without the first and last char, so "Hello" yields "ell". The
#string length will be at least 2.
def without_end(string):
	string = string[1:-1]
	return string


##In this exercise, your function will receive 3 parameters,
##a string and two integers.  The function will return the
##slice of the string starting from the index of the first
##number and going to the end.
##It will step through the string using the second number.
def partstring2(string, a, c):
	string = string[a:len(string)-1:c]
	return string

#Write a function that receives a number n as a parameter, return True
#if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in
#which case return True if the number is less or equal to 1, or greater
#or equal to 10.
def in1to10(n, outside_mode):
	if outside_mode == True:
		if n <= 1 or n >= 10:
			return True
		return False
	else:
		if n >= 1 and n <= 10:
			return True
		return False

##In this exercise, your function will receive two parameters.
##The first is a string, and the second is an index into
##the string.  The function returns a copy of the string
##without the character at the index specified.
def missing_char(string, index):
	string = string[:index] + string[index + 1:]
	return string

#Given a string, return the string made of its first two chars, so the
#String "Hello" yields "He". If the string is shorter than length 2,
#return whatever there is, so "X" yields "X", and the empty string ""
#yields the empty string "".
def first_two(string):
	if len(string) < 2:
		return string
	else:
		return string[0:2]

##This function recieves a string parameter.  It will check
##if the substrings `cat` and `dog` appear the same number
##of times in the string.  It returns a boolean value
##indicating if they are the same or not.
def cat_dog(string):
	c_count = string.count("cat")
	d_count = string.count("dog")
	if c_count == d_count:
		return True
	return False
