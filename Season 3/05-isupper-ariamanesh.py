inStr=input()
upperCharsCount = 0;
lowerCharsCount = 0;

for letter in inStr:
	if(letter.isupper()):
		upperCharsCount = upperCharsCount + 1;
	else:
		lowerCharsCount = lowerCharsCount + 1;

if(upperCharsCount > lowerCharsCount):
	print(inStr.upper())
else:
	print(inStr.lower())