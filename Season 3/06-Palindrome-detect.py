inStr = input().lower()

if(inStr == inStr[::-1]): # reversing a string
	print('palindrome');
else:
	print('not palindrome');